import random


class Ai:
    def __init__(self, canvas):

        self.canvas = canvas

        self.distance_to_line_e, \
            self.distance_to_line_s, \
            self.distance_to_line_w, \
            self.distance_to_line_n = self.canvas.get_player_distances()

        self.weight_of_n, self.weight_of_e, self.weight_of_s, self.weight_of_w = (0.25, 0.25, 0.25, 0.25)

        self.reward_for_north, self.reward_for_east, self.reward_for_south, self.reward_for_west = (0, 0, 0, 0)

        self.collided = False

        self.num_batch_size = 0
        self.total_batch_size = 10
        self.num_trains = 0
        self.total_num_trains = 100000

        self.movement_diff = 1

        self.num_moves_n, self.num_moves_e, self.num_moves_w, self.num_moves_s = (0, 0, 0, 0)

        self.average_reward_n, self.average_reward_e, self.average_reward_w, self.average_reward_s = (0, 0, 0, 0)

        self.max_num_movements = 5000
        self.movement_counter = 0

    # CERTAIN COMMENTS IN CODE NEED TO BECOME ACTUAL METHODS OTHERWISE BIG BUST
    # First try program will randomly try certain actions with a certain number of dots( lets just say 10)

    # CRA(Complete Random Action)
    # RA(Reward Action )

    # Over time the randomness will decrease
    # Also for every action it will give u a reward for that specific action
    # 10 points (cumulatively) for every movement where it doesnt hit an object
    # -500 points for every time it hits a wall, and it forces the specific action path to end

    # For each training montage, the 10 circles will do their random shit, and die, and we will take their point totals
    # and say, we recommend this action first,
    # Overall Randomness(or the probability the program chooses to randomize the movements, or choose the path that is
    # based on a reward system )
    # FIRST HALF OF TRAINING should choose random paths more, and as it approaches the halfway point, it should be
    # choose the random path less and less
    # SECOND HALF OF TRAINING should rely more the reward system/ neural network we created during the first half of
    # training

    def move(self, direction):
        if not self.canvas.move_player(direction):
            self.collided = True

    def tick(self):
        while self.num_trains < self.total_num_trains + 1 and self.canvas.is_running():
            self.reward_for_north = 0
            self.reward_for_east = 0
            self.reward_for_south = 0
            self.reward_for_west = 0
            self.num_trains = self.num_trains + 1
            print(f"Gen #{self.num_trains}")
            self.num_batch_size = 1
            while self.num_batch_size < self.total_batch_size + 1 and self.canvas.is_running():
                # PlayerObject hits a big ass wall or reaches the goal
                self.num_batch_size = self.num_batch_size + 1
                print(f"PlayerObject #{self.num_batch_size}")
                while self.movement_counter < self.max_num_movements and self.canvas.is_running():
                    self.movement_counter = self.movement_counter + 1
                    self.collided = False
                    type_of_action = random.randint(1, 100)  # 5+randomovement,5+rewardmovement

                    if type_of_action > 50:
                        # Actions based on pure and utter randomness (Meant for exploration)
                        direction = random.randint(0, 3)
                        if direction == 0:
                            print("Random Up")
                            self.move(3)
                            self.num_moves_n = self.num_moves_n + 1
                            self.create_rewards_n()
                        if direction == 1:
                            print("Random Right")
                            self.move(0)
                            self.num_moves_e = self.num_moves_e + 1
                            self.create_rewards_e()
                        if direction == 2:
                            print("Random Down")
                            self.move(1)
                            self.num_moves_s = self.num_moves_s + 1
                            self.create_rewards_s()
                        if direction == 3:
                            print("Random Left")
                            self.move(2)
                            self.num_moves_w = self.num_moves_w + 1
                            self.create_rewards_w()

                    else:  # Actions based on Weighting and Rewards (the actual neural network)

                        n_weight = self.weight_of_n * 100
                        s_weight = self.weight_of_s * 100
                        e_weight = self.weight_of_e * 100
                        w_weight = self.weight_of_w * 100

                        v = random.randint(1, 100)
                        if v <= n_weight:
                            print("Action Up")
                            self.move(3)
                            self.num_moves_n = self.num_moves_n + 1
                            self.create_rewards_n()
                        elif v <= e_weight:
                            print("Action Right")
                            self.move(0)
                            self.num_moves_e = self.num_moves_e + 1
                            self.create_rewards_e()
                        elif v <= s_weight:
                            print("Action Down")
                            self.move(1)
                            self.num_moves_s = self.num_moves_s + 1
                            self.create_rewards_s()
                        else:
                            print("Action Left")
                            self.num_moves_w = self.num_moves_w + 1
                            self.move(2)
                            self.create_rewards_w()

            self.adjust_weights()

    def adjust_weights(self):
        self.average_reward_n = self.reward_for_north / self.num_moves_n
        self.average_reward_e = self.reward_for_east / self.num_moves_e
        self.average_reward_s = self.reward_for_south / self.num_moves_s
        self.average_reward_w = self.reward_for_west / self.num_moves_w

        if self.average_reward_n > 10:
            self.weight_of_n = self.weight_of_n + 0.12
            self.weight_of_e = self.weight_of_e - 0.04
            self.weight_of_s = self.weight_of_s - 0.04
            self.weight_of_w = self.weight_of_w - 0.04
        elif self.average_reward_n > 5:
            self.weight_of_n = self.weight_of_n + 0.06
            self.weight_of_e = self.weight_of_e - 0.02
            self.weight_of_s = self.weight_of_s - 0.02
            self.weight_of_w = self.weight_of_w - 0.02
        elif self.average_reward_n < 0:
            self.weight_of_n = self.weight_of_n - 0.21
            self.weight_of_e = self.weight_of_e + 0.07
            self.weight_of_s = self.weight_of_s + 0.07
            self.weight_of_w = self.weight_of_w + 0.07

        if self.average_reward_e > 10:
            self.weight_of_n = self.weight_of_n - 0.04
            self.weight_of_e = self.weight_of_e + 0.12
            self.weight_of_s = self.weight_of_s - 0.04
            self.weight_of_w = self.weight_of_w - 0.04
        elif self.average_reward_e > 5:
            self.weight_of_n = self.weight_of_n - 0.02
            self.weight_of_e = self.weight_of_e + 0.06
            self.weight_of_s = self.weight_of_s - 0.02
            self.weight_of_w = self.weight_of_w - 0.02
        elif self.average_reward_e < 0:
            self.weight_of_n = self.weight_of_n + 0.07
            self.weight_of_e = self.weight_of_e - 0.21
            self.weight_of_s = self.weight_of_s + 0.07
            self.weight_of_w = self.weight_of_w + 0.07

        if self.average_reward_s > 10:
            self.weight_of_n = self.weight_of_n - 0.04
            self.weight_of_e = self.weight_of_e - 0.04
            self.weight_of_s = self.weight_of_s + 0.12
            self.weight_of_w = self.weight_of_w - 0.04
        elif self.average_reward_s > 5:
            self.weight_of_n = self.weight_of_n - 0.02
            self.weight_of_e = self.weight_of_e - 0.02
            self.weight_of_s = self.weight_of_s + 0.06
            self.weight_of_w = self.weight_of_w - 0.02
        elif self.average_reward_s < 0:
            self.weight_of_n = self.weight_of_n + 0.07
            self.weight_of_e = self.weight_of_e + 0.07
            self.weight_of_s = self.weight_of_s - 0.21
            self.weight_of_w = self.weight_of_w + 0.07

        if self.average_reward_w > 10:
            self.weight_of_n = self.weight_of_n - 0.04
            self.weight_of_e = self.weight_of_e - 0.04
            self.weight_of_s = self.weight_of_s - 0.04
            self.weight_of_w = self.weight_of_w + 0.12
        elif self.average_reward_s > 5:
            self.weight_of_n = self.weight_of_n - 0.02
            self.weight_of_e = self.weight_of_e - 0.02
            self.weight_of_s = self.weight_of_s - 0.02
            self.weight_of_w = self.weight_of_w + 0.06
        elif self.average_reward_s < 0:
            self.weight_of_n = self.weight_of_n + 0.07
            self.weight_of_e = self.weight_of_e + 0.07
            self.weight_of_s = self.weight_of_s + 0.07
            self.weight_of_w = self.weight_of_w - 0.21

    def closer_than(self, i=5):
        for distance in self.canvas.get_player_distances():
            if distance < i:
                return True
        return False

    def create_rewards_n(self):
        if self.closer_than(5):
            self.reward_for_north = self.reward_for_north + 10
        elif self.collided:
            self.reward_for_north = self.reward_for_north - 200
        else:
            self.reward_for_north = self.reward_for_north + 20

    def create_rewards_e(self):
        if self.closer_than(5):
            self.reward_for_east = self.reward_for_east + 15
        elif self.collided:
            self.reward_for_east = self.reward_for_east - 200
        else:
            self.reward_for_east = self.reward_for_east + 30

    def create_rewards_s(self):
        if self.closer_than(5):
            self.reward_for_south = self.reward_for_south + 10
        elif self.collided:
            self.reward_for_south = self.reward_for_south - 200
        else:
            self.reward_for_south = self.reward_for_south + 20

    def create_rewards_w(self):
        if self.closer_than(5):
            self.reward_for_west = self.reward_for_west + 10
        elif self.collided:
            self.reward_for_west = self.reward_for_west - 200
        else:
            self.reward_for_west = self.reward_for_west + 20

    def gui(self):
        return f"N: {self.average_reward_n} E: {self.average_reward_e} " \
            f"S: {self.average_reward_s} W: {self.average_reward_w}"

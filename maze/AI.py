#input variables
import random
distanceToLineN =0
distanceToLineE =0 # BRYSENS DATA FROM THE MAIN PYGAME CLASS WILL FILL THIS IN
distanceToLineS =0
distanceToLineW =0
weightOfN=0.25
weightOfE=0.25
weightOfS=0.25
weightOfW=0.25
rewardforNorth=0
rewardforEast=0
rewardforSouth=0
rewardforWest=0
hasCollided= False # BRYSENS DATA WILL FILL THIS STUFF IN
numbatchsize=0
totalbatchsize=10
numTrains=0
totalnumTrains= 10
MovementDiff=1
numMovesN=0
numMovesE=0
numMovesS=0
numMovesW=0
AverageNorthReward=0
AverageEastReward=0
AverageSouthReward=0
AverageWestReward=0
MaxNumofMovements=26
movementCounter=0



#CERTAIN COMMENTS IN CODE NEED TO BECOME ACTUAL METHODS OTHERWISE BIG BUST
#First try program will randomly try certain actions with a certian number of dots( lets just say 10)


#CRA(Complete Random Action)
#RA(Reward Action )


#Over time the randomness will decrease
#Also for every action it will give u a reward for that specfic action
#10 points (cumutlvielty) for every movement where it doesnt hit an object
# -500 points for every time it hits a wall, and it forces the specifc action path to end

#For each training montage, the 10 circles will do thier random shit, and die, and we will take thier point totals
#and say, we reocmmend this action first,
#Overall Randomness(or the probability the program chooses to randomonzie the movments, or choose the path that is based on a reward system )

'''FIRST HALF OF TRAING should choose random paths more, and as it approaches the halfway point, it should be choose the random path less and less
SECOND HALF OF TRANING should rely more the reward system/ neural network we created during the first half of training'''



while(numTrains < totalnumTrains+1):
    rewardforNorth=0
    rewardforEast=0
    rewardforSouth=0
    rewardforWest=0
    numTrains=numTrains+1
    print("Gen #"+str(numTrains))
    numbatchsize=1
    while((numbatchsize<totalbatchsize)+1):  #PlayerObject hits a big ass wall or reaches the goal):
        numbatchsize = numbatchsize + 1
        print("PlayerObject #"+str(numbatchsize))
        while(movementCounter<MaxNumofMovements):
            movementCounter=movementCounter+1

            typeOfAction=random.randint(1,100)  #5+randomovement,5+rewardmovement

            if(typeOfAction>MovementDiff+(5*numTrains)): #Actions based on pure and utter randomness(Meant for exploration )
                CRA=random.randint(1,4)
                if(CRA==1):
                    #MoveNorth
                    numMovesN=numMovesN+1
                    CreateRewardsN()
                    print("North")
                if(CRA==2):
                    #Move East
                    numMovesE=numMovesE+1
                    CreateRewardsE()
                    print("East")
                if(CRA==3):
                    #Move South
                    numMovesS=numMovesS+1
                    CreateRewardsS()
                    print("South")
                if(CRA==4):
                    #Move West
                    numMovesW=numMovesW+1
                    CreateRewardsW()
                    print("West")
            else:  #Actions based on Weighting and Rewards( the actual neural network)

                NorthWeight=weightOfN*100
                SouthWeight=weightOfS*100
                EastWeight=weightOfE*100
                WestWeight=weightOfW*100


                RA=random.randint(1,100)
                if(RA>0 and RA<=NorthWeight):
                    #Move North
                    numMovesN=numMovesN+1
                    CreateRewardsN()
                if(RA>NorthWeight and RA<=EastWeight):
                    #Move East
                    numMovesE=numMovesE+1
                    CreateRewardsE()
                if(RA>EastWeight and RA<=SouthWeight):
                    #Move South
                    numMovesS=numMovesS+1
                    CreateRewardsS()
                if(RA>SouthWeight and RA<=100):
                    numMovesW=numMovesW+1
                    #Move West
                    CreateRewardsW()

    AdjustWeights()



def AdjustWeights():
    AverageNorthReward = (rewardforNorth/numMovesN)
    AverageEastReward  = (rewardforEast/numMovesE)
    AverageSouthReward = (rewardforSouth/numMovesS)
    AverageWestReward  = (rewardforWest/numMovesW)

    if((AverageNorthReward)>10):
        weightOfN=weightOfN+0.12
        weightOfE=weightOfE-0.04
        weightOfS=weightOfS-0.04
        weightOfW=weightOfW-0.04
    elif((AverageNorthReward)>5):
        weightOfN=weightOfN+0.06
        weightOfE=weightOfE-0.02
        weightOfS=weightOfS-0.02
        weightOfW=weightOfW-0.02
    elif((AverageNorthReward)<0):
        weightOfN=weightOfN-0.21
        weightOfE=weightOfE+0.07
        weightOfS=weightOfS+0.07
        weightOfW=weightOfW+0.07

    if((AverageEastReward)>10):
        weightOfN=weightOfN-0.04
        weightOfE=weightOfE+0.12
        weightOfS=weightOfS-0.04
        weightOfW=weightOfW-0.04
    elif((AverageEastReward)>5):
        weightOfN=weightOfN-0.02
        weightOfE=weightOfE+0.06
        weightOfS=weightOfS-0.02
        weightOfW=weightOfW-0.02
    elif((AverageEastReward)<0):
        weightOfN=weightOfN+0.07
        weightOfE=weightOfE-0.21
        weightOfS=weightOfS+0.07
        weightOfW=weightOfW+0.07

    if((AverageSouthReward)>10):
        weightOfN=weightOfN-0.04
        weightOfE=weightOfE-0.04
        weightOfS=weightOfS+0.12
        weightOfW=weightOfW-0.04
    elif((AverageSouthReward)>5):
        weightOfN=weightOfN-0.02
        weightOfE=weightOfE-0.02
        weightOfS=weightOfS+0.06
        weightOfW=weightOfW-0.02
    elif((AverageSouthReward)<0):
        weightOfN=weightOfN+0.07
        weightOfE=weightOfE+0.07
        weightOfS=weightOfS-0.21
        weightOfW=weightOfW+0.07

    if((AverageWestReward)>10):
        weightOfN=weightOfN-0.04
        weightOfE=weightOfE-0.04
        weightOfS=weightOfS-0.04
        weightOfW=weightOfW+0.12
    elif((AverageSouthReward)>5):
        weightOfN=weightOfN-0.02
        weightOfE=weightOfE-0.02
        weightOfS=weightOfS-0.02
        weightOfW=weightOfW+0.06
    elif((AverageSouthReward)<0):
        weightOfN=weightOfN+0.07
        weightOfE=weightOfE+0.07
        weightOfS=weightOfS+0.07
        weightOfW=weightOfW-0.21


def CreateRewardsN():
            if((distancetoLineN or distanceToLineE or distanceToLineS or distanceToLineW) < 5):
                rewardforNorth=rewardforNorth+10
            elif(hasCollided):
                rewardforNorth=rewardforNorth-200
            else:
                rewardforNorth=rewardforNorth+20
def CreateRewardsE():
            if((distancetoLineN or distanceToLineE or distanceToLineS or distanceToLineW) < 5):
                rewardforEast=rewardforEast+15
            elif(hasCollided):
                rewardforEast=rewardforEast-200
            else:
                rewardforEast=rewardforEast+30
def CreateRewardsS():
            if((distancetoLineN or distanceToLineE or distanceToLineS or distanceToLineW) < 5):
                rewardforSouth=rewardforSouth+10
            elif(hasCollided):
                rewardforSouth=rewardforSouth-200
            else:
                rewardforSouth=rewardforSouth+20

def CreateRewardsW():
            if((distancetoLineN or distanceToLineE or distanceToLineS or distanceToLineW) < 5):
                rewardforWest=rewardforWest+10
            elif(hasCollided):
                rewardforWest=rewardforWest-200
            else:
                rewardforWest=rewardforWest+20


while(numTrains < totalnumTrains+1):
    rewardforNorth=0
    rewardforEast=0
    rewardforSouth=0
    rewardforWest=0
    numTrains=numTrains+1
    print("Gen #"+str(numTrains))
    numbatchsize=1
    while((numbatchsize<totalbatchsize+1) or #PlayerObject hits a big ass wall or reaches the goal):
        numbatchsize=numbatchsize+1
        print("PlayerObject #"+str(numbatchsize))
        while(movementCounter<MaxNumofMovements):
            movementCounter=movementCounter+1

            typeOfAction=random.randint(1,100)  #5+randomovement,5+rewardmovement

            if(typeOfAction>MovementDiff+(5*numTrains)): #Actions based on pure and utter randomness(Meant for exploration )
                CRA=random.randint(1,4)
                if(CRA==1):
                    #Move N
                    numMovesN=numMovesN+1
                    CreateRewardsN()
                    print("North")
                if(CRA==2):
                    #Move East
                    numMovesE=numMovesE+1
                    CreateRewardsE()
                    print("East")
                if(CRA==3):
                    #Move South
                    numMovesS=numMovesS+1
                    CreateRewardsS()
                    print("South")
                if(CRA==4):
                    #Move West
                    numMovesW=numMovesW+1
                    CreateRewardsW()
                    print("West")
            else:  #Actions based on Weighting and Rewards( the actual neural network)

                NorthWeight=weightOfN*100
                SouthWeight=weightOfS*100
                EastWeight=weightOfE*100
                WestWeight=weightOfW*100


                RA=random.randint(1,100)
                if(RA>0 and RA<=NorthWeight):
                    #Move North
                    numMovesN=numMovesN+1
                    CreateRewardsN()
                if(RA>NorthWeight and RA<=EastWeight):
                    #Move East
                    numMovesE=numMovesE+1
                    CreateRewardsE()
                if(RA>EastWeight and RA<=SouthWeight):
                    #Move South
                    numMovesS=numMovesS+1
                    CreateRewardsS()
                if(RA>SouthWeight and RA<=100):
                    numMovesW=numMovesW+1
                    #Move West
                    CreateRewardsW()

    AdjustWeights()

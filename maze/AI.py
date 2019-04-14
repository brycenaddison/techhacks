#input variables
import random
distanceToLineN =0
distanceToLineE =0 # These values will be given from the main python class.
distanceToLineS =0
distanceToLineW =0
weightOfN=0.25
weightOfE=0.25
weightOfS=0.25
weightofW=0.25
hasCollided= False
numbatchsize=0
totalbatchsize=10
numTrains=0
totalnumTrains= 10



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
     numTrains=numTrains+1
    print("Gen #"+str(numTrains))
    numbatchsize=1
    while((numbatchsize<totalbatchsize+1) or #PlayerObject hits a big ass wall or reaches the goal):
        numbatchsize=numbatchsize+1
        print("PlayerObject #"+str(numbatchsize))
        typeOfAction=random.randint(1,10)  #5+randomovement,5+rewardmovement
        if(typeOfAction>5): #Actions based on pure and utter randomness(Meant for exploration )
            CRA=random.randint(1,4)
            if(CRA==1):
                #Move N
                #Update state
                #Add award
                print("North")
            if(CRA==2):
                #Move East
                #Update State
                #Add award
                print("East")
            if(CRA==3):
                #Move South
                #Update State
                #Add award+10
                print("South")
            if(CRA==4):
                #Move West
                #Update state
                #Add award
                print("West")
        if(typeOfAction<5):  #Actions based on Weighting and Rewards( the actual neural network)

            NorthWeight=weightOfN*100
            SouthWeight=weightOfS*100
            EastWeight=weightOfE*100
            WestWeight=weightOfW*100


            RA=random.randint(1,100)
            if(RA>0 and RA<=NorthWeight):
                #Move North
                #Add award
            if(RA>NorthWeight and RA<=0.50):
                #Move East
                #Add award+10
            if(RA>0.5 and RA<=0.75):
                #Move South
                #Add award
            if(RA>
                #Move West
                #Add award

def CreateRewards():


            #if( (distancetoLineN or distanceToLineE or distanceToLineS or distanceToLineW) <25):
                #totalreward+=10
            #elif(hasCollided):
                #totalreward-=500
                #End Singular Batch
            #else:
                #totalreward=+20





#if(distancetoLineE and distanceToLineN and  distanceToLineS and distanceToLineW<25 )

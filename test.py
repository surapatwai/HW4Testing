## 57113045-9 :
##  Surapat Waiwattanakorn
##
##
##
import datetime
datetime.datetime.now().isoformat()
mynums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
index = 6;
## ANSWER Q1.a
print(mynums[6]);
## ANSWER Q1.b
for i in mynums:
    if(i<1):
        print(i)
## ANSWER Q2.a
list = []
for  i in range(-13,14):
    list.append(i)
    
print(list)

## ANSWER Q2.b
##
from random import randint 
list2 = []
for i in range(20):
    list2.append(randint(1,12))
print(list2)

## ANSWER Q2.c
##
myTest = [-38, 72, -33, 18, 96, -83, 57, 41]
myTotal = sum(myTest)
print(myTotal)

## ANSWER Q2.d
##

def average(numbers):
    return (sum(numbers)/len(numbers))
    
mynums = [i for i in range(51,101,5) ]
print(mynums)
print(average(mynums))

NZ_COINS = { "10c": 0.10, "20c": 0.20, "50c": 0.50, "1$": 1, "2$": 2 } 

## mypiggy keeps the number of NZ coins 
mypiggy  = { "20c": 11, "2$": 4, "10c": 5, "1$": 12 }
## ANSWER Q3.a
##  
print(mypiggy["20c"]+mypiggy["2$"]+mypiggy["10c"]+mypiggy["1$"])

## ANSWER Q3.b
## 
print(mypiggy["20c"]*NZ_COINS["20c"]+mypiggy["2$"]*NZ_COINS["2$"]+mypiggy["10c"]*NZ_COINS["10c"]+mypiggy["1$"]*NZ_COINS["1$"])



class Die(object):
    def __init__(self):

        self.__face = randint(1,6)
    @property
    def face(self):

        return self.__face
    
    def roll(self):
        self.__face = randint(1,6)
        
    def __str__(self):

        return ( "Die face: {}".format(self.__face) )
## ANSWER Q4.a
##
##
my2dice = [Die(),Die()]
print(my2dice[0].face+my2dice[1].face)

def printDiceStat( numberRolls ):

    die = Die()
    counts = [0, 0] 
    
    
    
    
    
    
            
    print("Number of rolls: {}".format(numberRolls)) 
    
    print("\n---------- Dice Stats -----------")    
    percentage = 100. * counts[0] / numberRolls
    print("face {} count: {:>3}, {:6.2f} %".format( "<= 3", counts[0], percentage )) 
    
    
    
    

#--- Test the def printDiceStat ---
rolls = 1000
printDiceStat( rolls )


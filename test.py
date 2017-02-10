## 57113045-9 :
##  Birds In-Sky 
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

## ANSWER Q1.c
##
myTest = [-38, 72, -33, 18, 96, -83, 57, 41]
myTotal = sum(myTest)
print(myTotal)
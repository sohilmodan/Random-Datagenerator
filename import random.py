import random
##from numpy import *


class Main: 
    print("Welcome")
    
    def generator(self):
        global coutry
        coutry= ['India','China','Japan','USA','UK','UAE']
        print(coutry)
        global cselect 
        cselect= random.choice((coutry))
        print(cselect)


    def age(self):
        if(cselect==coutry[0]):
            age=random.randrange(10,70)
            print(age)
        elif(cselect==coutry[1]):
            age=random.randrange(10,65)
            print(age)
        elif(cselect==coutry[2]):
            age=random.randrange(10,60)
            print(age)
        elif(cselect==coutry[3]):
            age=random.randrange(10,65)
            print(age)
        elif(cselect==coutry[4]):
            age=random.randrange(10,60)
            print(age)
        elif(cselect==coutry[5]):
            age=random.randrange(10,60)
            print(age)

c_reference=Main()
c_reference.generator()
c_reference.age()
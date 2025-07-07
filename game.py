import random
'''
1 for snake
-1 for water
0 for gun
'''
computer= random.choice([1,-1,0])
your= input("Enter your choice: ")
yourdict={"s": 1, "w":-1,"g":0} 

you = yourdict[your]

if(computer == you):
    print("Its Draw")
else:
    if(computer==-1 and you==1):
        print("You Win")
    elif(computer==1 and you==-1):
        print("You Lose")
    elif(computer==0 and you==1):
        print("You Win")
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==1 and you==1):
        print("You Win")
    
    else:
        ("Wrong")
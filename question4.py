from random import randint
number=randint(1,100) 
attempts=0
while True:
    guess=input("enter your guess")
    guess=int(guess)
    attempts+=1

    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    else:
        print("correct")    
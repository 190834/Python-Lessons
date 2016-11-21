import random
number= random.randint(1, 10)
print ("Guess a number from 1-10")

while True:
    guess=int (input("Guess:"))

    if guess>number:
        print ("Your guess is too high")

    elif guess<number:
        print ("Your guess is too low")
    elif guess == number:
     print ("correct")
    if guess==number:
        print (str([guess]))
        break



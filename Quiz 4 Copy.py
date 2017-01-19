score = 0
filename= 'Quiz.txt'
file = open(filename, "r")

print ("HAA Chapter 5 Test")
input("Press enter to continue")

#Question 1
for line in range(1,7):
    print (file.readline())
ans = input("What is your answer?")
if ans == '2':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 2
for line in range(8,15):
    print (file.readline())
ans = input("What is your answer?")
if ans == '4':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 3
for line in range(15,23):
    print (file.readline())
ans = input("What is your answer?")
if ans == '1':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 4
for line in range(22,28):
    print (file.readline())
ans = input("What is your answer?")
if ans == '1':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 5
for line in range(29,36):
    print (file.readline())
ans = input("What is your answer?")
if ans == '2':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 6
for line in range(36,44):
    print (file.readline())
ans = input("What is your answer?")
if ans == '3':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 7
for line in range(43,49):
    print (file.readline())
ans = input("What is your answer?")
if ans == '2':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 8
for line in range(50,57):
    print (file.readline())
ans = input("What is your answer?")
if ans == '4':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 9
for line in range(57,65):
    print (file.readline())
ans = input("What is your answer?")
if ans == '3':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 10
for line in range(64,71):
    print (file.readline())
ans = input("What is your answer?")
if ans == '1':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 11
for line in range(71,78):
    print (file.readline())
ans = input("What is your answer?")
if ans == '1':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 12
for line in range(78,84):
    print (file.readline())
ans = input("What is your answer?")
if ans == '1':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 13
for line in range(85,92):
    print (file.readline())
ans = input("What is your answer?")
if ans == '4':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 14
for line in range(93,100):
    print (file.readline())
ans = input("What is your answer?")
if ans == '1':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

#Question 15
for line in range(99,108):
    print (file.readline())
ans = input("What is your answer?")
if ans == '1':
    print('Good')
    score = score+1
else:
    print('Wrong')
    score = score+0

print ("You got", (score),"out of 15")

##IF ELSE

#vScore=75

#if vScore >=50:
#    print("\nPASS")
#else:
#    print("\nFail")

    ## IF N
#    vMonth="September"
#    vLetter="e"
#if vLetter in vMonth:
#    print ("There is a letter"), (vLetter), ("in"), (vMonth)
#else:
#    print("There is NOT a letter"), (vLetter), ("in"), (vMonth)

#vChoice=input("Enter Number 1 to 3:")

#if vChoice =="1":
#    print ("Chosen Item 1")
#if vChoice =="2":
#    print ("Chosen Item 2")
#if vChoice =="1":
#    print ("Chosen Item 3")
#Some unknown value has been entered else:
#else:
#    print("Sorry. You suck.")

#a=5
# a = 5
# e = 4
# i = 3
# o = 2
# u = 1

vWord = input ("Enter a word")

 #Convert the word into lower case

vWord = vWord.lower ()

 #Set score to be 0
score = 0

 #Create a loop so that
 #letters are looked at one by one...
for letter in vWord:
    if letter == "a":
        score = score+5
        print (letter, "is worth 5")
    elif letter == "e":
        score = score+4
        print (letter, "is worth 4")
    elif letter == "i":
        score = score+3
        print (letter, "is worth 3")
    elif letter == "o":
        score = score+2
        print (letter, "is worth 2")
    elif letter == "u":
        score = score+1
        print (letter, "is worth 1")
    else:
        print(letter, "is worth 0")

print ("Total score is", score)




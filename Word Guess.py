word=str(input("Player one, please enter a word"))
print ("Note, 0 is the first letter, 1 is the second and so on...")
print ("This word has", len(word), "letters")
guess=str(input("What is your guess?"))


while guess!=word:
   letter= str(input("This is incorrect, guess a letter"))
   if letter in word:
       print ("This letter is at", word.index(letter))
       guess=str(input("Guess the word again"))
   if letter not in word:
       print ("This letter is not in the word, guess again.")




if guess==word:
   print ("You got it!")

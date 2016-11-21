#vPrice = float(16.90)
#print("Price of chocolate is"),(vPrice)
#payed = int (input("Please enter cash"))


#print("you payed"),(payed)


#if payed > vPrice:
#   change = payed-vPrice
#   print("Your change is"),(payed-vPrice)
#if payed < vPrice:
#   print("That is not enough")

vPrice= float(input("Please enter the price of the chocolate you want"))
print (vPrice)

vCash= float(input(input("Please enter the cash of the chocolate you want:")))

vChangeDue= vCash-vPrice
vChangeGiven = round (vChangeDue,2)
print ("TRANSACTION SUMMARY MY FUCTION")
print ("Price of chocolate", vPrice)
print ("Cash Paid, vCash")

print ("Change Due",round (vChangeDue,2))
print ("Total Change Given:", vChangeGiven)

while vChangeDue >= 50:
   vChangeGiven = vChangeGiven+50
   vChangeDue=vChangeDue - 50
   print ("Giving out $50 note")
while vChangeDue >= 20:
   vChangeGiven = vChangeGiven+20
   vChangeDue=vChangeDue - 50
   print ("Giving out $20 note")
while vChangeDue >= 10:
   vChangeGiven = vChangeGiven+10
   vChangeDue=vChangeDue - 10
   print ("Giving out $10 note")
while vChangeDue >= 5.0:
   vChangeGiven = vChangeGiven+5.0
   vChangeDue=vChangeDue - 5.0
   print ("Giving out $5 note")
while vChangeDue >= 2.0:
   vChangeGiven = vChangeGiven+2.0
   vChangeDue=vChangeDue - 2.0
   print ("Giving out $2 coin")
while vChangeDue >= 1.0:
   vChangeGiven = vChangeGiven+2.0
   vChangeDue=vChangeDue - 1.0
   print ("Giving out $1 coin")

#list
fruitList = ["apple", "orange", "banana", "grape", "tomato", "mango"]
print (fruitList [0])

#Concatenation
numberList1 = [1,2,3]
numberList2 = [6,7,8]
numberList3 = numberList1+numberList2
print(numberList3)

numberList =[1,2,3]
print (numberList * 3)

#Slicing
print (fruitList[2:5])
print (fruitList[:4])
print (fruitList[5:])

#Replace position
fruitList[1] = "KIWI"
print (fruitList)

olympicList = [["Londen",2012]],[["Beijing",2008]],[["Athens", 2004]]
print (olympicList)
print (olympicList[0])

inventoryList = ["sword","armour","shield","healing potion"]
print (inventoryList)
inventoryList.append ("cabbage")
inventoryList.insert(2,"apple")
print (inventoryList)

#sort
print (inventoryList)
inventoryList.sort()
print(inventoryList)

#count
print(inventoryList)
print(inventoryList.count("sword"))

#Extend
print(inventoryList)
print(fruitList)
inventoryList.extend(fruitList)
print(inventoryList)
print(fruitList)

#Pop
print(fruitList)
vFruit = fruitList.pop(0) #remove last element
print(fruitList)
print(vFruit)

#remove
print(fruitList)
fruitList.remove("banana")#remove first occurance of an elemnt
print (fruitList)

#reverse
print(fruitList)
fruitList.reverse()
print(fruitList)

##Index
#print(fruitList)
#v_index = fruitList.index ("banana")#position of banana in the list
#print(v_index)

#Length
print(fruitList)
print (len(fruitList)) #length of list

#In
print("apple"in fruitList)

#Min/Max
print(min(fruitList))
print (max(fruitList))

#def hello():
#    print ("""
#    hi """)
#print (hello())

def f_sum(int1,int2):
        """This function will add two numbers"""
        return int1+int2
## Main Program##
vTotal = f_sum (20,15)
print("The total is:",vTotal)

def f_print_largest (int1,int2):
    """This function will print the largest of two integers"""
    if int1>int2:
        print(int1, "is the largest")
    if int1<int2:
         print(int2,"is the largest")
vNumber = (f_print_largest(20,15))


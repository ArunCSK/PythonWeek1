#array
from array import *

#access array element with index
def array():
    a = [2,3,4,6,5]
    for i in a:
        print(i)

    print("Array Elements:",a)
    index = int(input("Enter array index: "))
    #print("Element at index "+ str(index) + ": " + str(a[index]) )
    print(a[index])
    

#reverse array element
def reversearray():
    a = [2,3,4,6,5]
    print("Array Elements:",a)
    reverse_array = a[::-1]
    print(reverse_array)

#find number of occurrence in array
def findelements():
    a = [1,2,2,3,3,3,4,5,5,6]
    print(a)
    val = int(input("Enter element value:"))
    count = 0
    for i in a:
        if val == i: 
            count += 1
    print("No of Occurrence: "+ str(count))    

def removeelement():
    a = [1,2,2,3,3,3,4,5,5,6]
    print(a)
    val = int(input("Enter element value:"))
    count = 0
    for i in a:
        if val == i and count == 0: 
            a.remove(i)
            count += 1
    print(a)

#accept user input options
io = input("1.index 2.reverse 3.find 4.remove Enter values:")

if io == "index":
    array()
elif io == "reverse":
    reversearray()
elif io == "find":
    findelements()    
elif io == "remove":
    removeelement()
else: 
    print('Execute Success!!!')
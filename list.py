
#sum all the item in list
def sum():
    l = [1,2,4,6,8,9]
    print("List:",l)
    result = 0
    for i in l:
        result += i
    print("sum of list :",result)

#multiply all the item in list
def multiply():
    l = [1,2,4,6,8,9]
    print("List:",l)
    result = 1
    for i in l:
        result *= i
    print("sum of list :",result)

#find smallest number in the list
def small():
    l = [4,6,8,9,3]
    print("List:",l)
    result = l[0]
    print(result)
    for i in l:
        for j in l:
            if i < j and i < result:
                result = i
            elif j < i and j < result:
                result = j

    print("sum of list :",result)

#check list length greater than 2 and check first and last element are same
def check():
    l = ['abc', 'xyz', 'aba', '1221']
    result = 0
    print("Sample List:", l)
    for i in l:
        if len(i) > 2 and i[0] == i[len(i)-1]:
            result += 1
    print("Expected Result:",result)

#sort list in tuple in increasing order consider last element for sorting
def sort():
    l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    newlist= []
    print("Sample List:", l)
    temp = l[0]
    #print(temp)
    newlist = sorted(l, key=lambda x: x[1])
    print("Expected Result:",newlist)
        
#accept user input options
io = input("1.sum 2.multiply 3.small 4.check 5.sort Enter values:")

if io == "sum":
    sum()
elif io == "multiply":
    multiply()
elif io == "small":
    small()    
elif io == "check":
    check()
elif io == "sort":
    sort()
else: 
    print('Execute Succes!!!')
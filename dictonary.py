from collections import OrderedDict

#sorting dict asc and desc
def sorting():
    dict = {}
    dict[2] = 12
    dict[1] = 54
    dict[3] = 47
    dict[5] = 96
    dict[4] = 45
    dict[6] = 15

    print("Ascending:")
    for i in sorted(dict.values()):
        print(i, end = " ")

    print("Descending:")
    for i in sorted(dict.values(),reverse = True):
        print(i,end = " ")

#dict add values
def adddictvalue():
    dict = {0: 10, 1: 20}
    print("Sample Dictionary: ", dict)
    dict[2] = 30
    print("Expected Result: ",dict)

#concat multiple dict
def Merge(dict1, dict2): 
    res = {**dict1, **dict2}
    return res 
    
def concat():
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50,6:60}
    print(dic1)
    print(dic2)
    print(dic3)
    merge1 = (Merge(dic1,dic2))
    merge2 = (Merge(merge1, dic3))
    print(merge2)

#loop dict
def loop():
    dict = {}
    dict[2] = 12
    dict[1] = 54
    dict[3] = 47
    dict[5] = 96
    dict[4] = 45
    dict[6] = 15

    for i in dict.values():
        print(i, end = " ")

#dict to print in range
def printrange():
    print('Sample Dictionary: ')
    dict = {}
    dict[2] = 12
    dict[1] = 54
    dict[3] = 47
    dict[5] = 96
    dict[4] = 45
    dict[6] = 15
    print(dict)
    n = int(input("Enter key: "))
    #d = dict{}
    print("{", end = " ")
    for key,val in dict.items():
        if key <= n:
            print( str(key)+": "+ str(val) , end = " "  )
    print("}")
            

#accept user input options
io = input("1.sort 2.add 3.concat 4.loop 5.print Enter values:")

if io == "sort":
    sorting()
elif io == "add":
    adddictvalue()
elif io == "concat":
    concat()    
elif io == "loop":
    loop()
elif io == "print":
    printrange()
else: 
    print('Execute Succes!!!')
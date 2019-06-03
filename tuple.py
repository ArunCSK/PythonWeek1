
#create tuple
def create():
    t = ("1","2","3")
    print("Tuple: ",t)

#create tuple with diff datatype
def data():
    t = ("ABC", 12, 23.34, True, 'c')
    print("Tuple: ",t)

#unpack tuple with sevral variable
def unpack():
    t= ("Arun", "Male", 9768265628,)
    print("Tuple: ",t)
    (Name, Gender, Phone) = t
    (Name1, Gender1, Phone1) = t
    print(Name, Name1)
    print(Gender, Gender1)
    print(Phone, Phone1)

#tuple colon
def colon():
    t = ("ABC", 12, 23.34, [], 'c')
    t[3].append("new value")
    print(t)

#print repeated items of tuple
def repeat():
    t = (1,1,1,2,2,3,3,4,4,4,4,5,5,6,7,8,9,9)
    print("Tuple: ",t)
    count = 0
    dict = {}
    for i in t:
        count = t.count(i)
        dict[i] = count
    print(dict)



#accept user input options
io = input("1.create 2.data (tuple with diff datatype) 3.unpack 4.colon 5.repeat Enter values:")

if io == "create":
    create()
elif io == "data":
    data()
elif io == "unpack":
    unpack()    
elif io == "colon":
    colon()
elif io == "repeat":
    repeat()
else: 
    print('Execute Succes!!!')

#create set
def createset():
    iset = {"1","2","3"}
    print("Sets: ",iset)

#iterate set
def iterate():
    iset = {"1","2","3"}
    print("Sets: ",iset)
    for val in iset:
        print(val)

#add set
def add():
    iset = {"1","2","3"}
    print("Sets: ",iset)
    item = input("Enter item to be add:")
    iset.add(item)
    print("Sets: ",iset)

#remove for set
def remove():
    iset = {"1","2","3"}
    print("Sets: ",iset)
    item = input("Enter item to be removed:")
    iset.remove(item)
    print("Sets: ",iset)

#remove for set if present
def check():
    iset = {"1","2","3"}
    print("Sets: ",iset)
    item = input("Enter item to be removed:")
    for val in iset:
        if val == item:
            iset.remove(item)
            break
    print("Sets: ",iset)
#accept user input options
io = input("1.create 2.iterate 3.add 4.remove 5.check Enter values:")

if io == "create":
    createset()
elif io == "iterate":
    iterate()
elif io == "add":
    add()    
elif io == "remove":
    remove()
elif io == "check":
    check()
else: 
    print('Execute Succes!!!')
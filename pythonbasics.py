#print('hi')

from datetime import date

#reverse string
def name():
    firstname = input('Enter First name')
    lastname = input('Enter Last Name')
    #print(firstname + ' ' + lastname)
    txt = firstname + ' ' + lastname
    reversetxt = reversestring(txt)
    newtxt = ""
    for t in reversetxt:
        newtxt += " " + t
    print(newtxt)

def reversestring(txt):
    return txt[::-1]

#list and tuple
def listntuple():
    inputstr = input("Sample data: ")
    l = (inputstr.split(","))
    t = tuple(l)
    print("List: ",l)
    print("Tuple: ", t)

#array to display first and last color
def color():
    color_list = ["Red","Green","White" ,"Black"]
    print("First:",color_list[0])
    print("Last:",color_list[len(color_list)-1])

#print python syntax and desc
def printsyntax():
    #import pydoc
    func = input('Sample function:')
    #print(func+".__doc__")
    print(help(func))
    
#print calender of given month and year
def printcalender():
    import calendar
    print(calendar.month(2019,5))

#Calculate date diff
def CalculateDateDiff():
    dates = input("Sample dates:")
    print(dates)
    

#accept user input options
io = input("1.name 2.list 3.color 4.syntax 5.calender Enter values:")
#print(io)

if io == "name":
    name()
elif io == "list":
    listntuple()
elif io == "color":
    color()    
elif io == "syntax":
    printsyntax()
elif io == "calender":
    printcalender()
elif io == "date":
    CalculateDateDiff()
else: 
    print('Execute Succes!!!')




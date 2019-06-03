
#find length of the string
def length():
    s = "arun"
    print("String:", s)
    print("String length :", len(s))

#count character frequency
def count():
    s = "google.com"
    print("String:", s)
    dict = {}
    count = 0
    for i in s:
        count = s.count(i)
        dict[i] = count
    #sorted(dict)
    print(dict)
    
#replace first occurence to $
def replace():
    s = "google"
    subs = s[1:len(s)]
    first = s[0]
    print(first, subs)
    print("Sample string:", s)
    subs = first + subs.replace(first,"$",1)
    print("Expected string:",  subs)

#add ing to the string if ing is peresnt than add ly. string length has be min 3
def add():
    s = "string"
    newstr = ""
    print("Sample Output:", s)
    spoint = len(s) - 3
    sub1 = s[0:spoint]
    sub2 = s[spoint:len(s)]
    if len(s) >= 3:
        if sub2 == "ing":
            newstr = s + "ly"
        else:
            newstr = s + "ing"
    print("Expected String:",newstr)

#find the longest length from given string
def long():
    n = int(input("Enter no. of string (Count): "))
    a = []
    for i in range(n):
        st = input("Enter string:")
        a.append(st)
    #print(a)
    lenofstr = 0
    val = ""
    for i in a:
        if len(i) > lenofstr:
            val = i 
            lenofstr = len(i)
    print("Longest string ", val ," length ",lenofstr)





#accept user input options
io = input("1.length 2.count 3.replace 4.add 5.long Enter values:")

if io == "length":
    length()
elif io == "count":
    count()
elif io == "replace":
    replace()    
elif io == "add":
    add()
elif io == "long":
    long()
else: 
    print('Execute Succes!!!')
#from itertools import permutations 

#probalility to draw ace from pack
def ace():
  cards = 52
  ace  = 4
  prob = ace/cards
  print("Card:",cards)
  print("Ace:", ace)
  print("Result:",round(prob,2))

def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)

def event_probability1(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) 
    return round(probability, 3)

#probalitity to draw ace after drawing king on first draw
def king():
    cards = 52
    cards_drawn = 1
    cards = cards - cards_drawn
    kings = 4
    prob = event_probability1(kings, cards)
    print("Card:",cards)
    print("No of aces drawn:",cards_drawn)
    print("No of cards:", cards)
    print("Result:",round(prob,2))

#probalitity to draw ace after drawing king on first draw
def aces():
    cards = 52
    cards_drawn = 1
    cards = cards - cards_drawn
    aces = 4
    aces_drawn = 1
    aces = aces - aces_drawn
    prob = event_probability(aces, cards)
    print("Card:",cards)
    print("No of aces drawn:",cards_drawn)
    print("No of cards:", cards)
    print("Result:",round(prob,2))

#probalitity to find coin tossed 3 times
def coin():
    #perm = permutations(["H", "T", "H"])
    #l = list(itertools.product("HT", repeat=3))
    #for i in list(perm):
    #    print(i)
    cointossed = [["H", "H", "H"], ["H", "H", "T"], ["H", "T", "T"], ["T", "T", "T"], 
    ["T", "T", "H"],["T", "H", "H"],["H", "T", "H"],["T", "H", "T"]]
    print(cointossed)
    length = len(cointossed)
    a = []
    headcount = 0
    hcount = 0
    for i in cointossed:
        headcount = 0
        for j in i :
            if j == "H":
                headcount += 1
        a.append(headcount)
        #print(a)
    for i in a:
        if i == 3:
            hcount += 1
    
    result = event_probability1(hcount, length)
    print("Probabality for 3 heads:", result)

    hcount = 0
    for i in a:
        if i > 0:
            hcount += 1
    result = event_probability1(hcount, length)
    print("Probabality for only 1 heads:", result)

    hcount = 0
    for i in a:
        if i == 2:
            hcount += 1
    result = event_probability1(hcount, length)
    print("Probabality for 2 heads:", result)

#probabality to check rainy and traffic to reach work
def rain():
    #rainy day and heavy traffic
    rtprob = 1212
    #heavy traffic
    tprob = 1414
    #no traffic and no rain
    latework = 1818

#accept user input options
io = input("1.ace 2.king 3.aces 4.coin 5.rain Enter values:")

if io == "ace":
    ace()
elif io == "king":
    king()
elif io == "aces":
    aces()    
elif io == "coin":
    coin()
elif io == "rain":
    inverse()
else: 
    print('Execute Succes!!!')
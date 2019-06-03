import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

#draw line
def line():
    x = np.linspace(0,2,2)
    plt.plot(x, x , label= 'linear')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.show()

#draw lines 
def lines():
    x = np.linspace(0,2,100)
    plt.plot(x, x**2, label= 'line')
    plt.xlabel('X-label')
    plt.ylabel('Y-label')
    plt.title("Simple Plot")
    plt.legend()
    plt.show()

#import co-ordinates from files
def files():
    x = []
    y = []
    with open('test1.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
        plt.plot(x, y ,label="file values")
        plt.xlabel('X-Label')
        plt.ylabel('Y-Label')
        plt.title('Test.txt file values')
        plt.legend()
        plt.show()

#print chart form fdata.csv
def fdata():
    date = []
    opened = []
    high = []
    low = []
    close = []
    xname = ''
    yname = ''
    with open('fdata.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            print(row)
            date.append(row[0])
            opened.append(row[1])
            high.append(row[2])
            low.append(row[3])
            close.append(row[4])
        #print(x, y)
        plt.plot(date[1:len(date)],opened[1:len(opened)],label="Open")
        plt.plot(date[1:len(date)],high[1:len(high)],label="High")
        plt.plot(date[1:len(date)],low[1:len(low)],label="Low") 
        plt.plot(date[1:len(date)],close[1:len(close)],label="Close")
        #plt.plot(date[1:len(date)],opened[1:len(opened)],label="Date")
        plt.xlabel(date[0])
        plt.ylabel(opened[0])
        plt.title('fdata.csv file values')
        plt.legend()
        plt.show()

#print chart form fdata.csv
def fdata1():
    df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
    df.plot()
    plt.show()

#print two or more line in chart with legends
def legends():
    x = [10,20,30]
    y = [40,50,60]
    plt.plot(x, y , label='line x and y')
    a = [100,50, 40]
    b = [30,20,10]
    plt.plot(a,b , label='line a and b')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('two lines')
    plt.legend()

    plt.show()

#accept user input options
io = input("1.line 2.lines 3.files 4.fdata 5.legends Enter values:")

if io == "line":
    line()
elif io == "lines":
    lines()
elif io == "files":
    files()    
elif io == "fdata":
    fdata1()
elif io == "legends":
    legends()
else: 
    print('Execute Success!!!')
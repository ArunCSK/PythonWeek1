
import matplotlib.pyplot as plt
import pandas as pd
import csv

#create a piechart
def piechart():
    lang = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
    popular = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    plt.pie(popular,labels = lang)
    plt.show()

#create a piechart with title
def title():
    lang = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
    popular = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    plt.pie(popular,labels = lang)
    plt.title("PopularitY of Programming Language", bbox={'facecolor':'0.8', 'pad':5})
    plt.show()    

#Display piechart data by reading csv file
def medal():
    df = pd.read_csv('medal.csv')
    country = df["country"]
    medal = df["gold_medal"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    explode = (0.1, 0, 0, 0, 0)
    plt.pie(medal, labels=country, explode=explode, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.show()

#accept user input options
io = input("1.piechart 2.title 3.medal Enter values:")

if io == "piechart":
    piechart()
elif io == "title":
    title()
elif io == "medal":
    medal()    
else: 
    print('Execute Success!!!')
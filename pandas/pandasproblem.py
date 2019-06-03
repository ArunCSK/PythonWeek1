#sudo apt-get install python-pandas
#sudo apt-get install python3-pandas
#sudo pip install pandas
import pandas as pd
import numpy as np

#one dimenstional array
def array():
    a = pd.Series([2,3,45,6,6])
    print(a)

#print array to list
def list():
    a = pd.Series([2,3,45,6,6])
    print(a)
    print(a.tolist())
    #print(type(a.tolist()))

#add, multiply, subtract, divide two pandas series
def math():
    a = pd.Series([2, 4, 6, 8, 10])
    b = pd.Series([1, 3, 5, 7, 9])
    r1 = a + b
    print("Addition:")
    print(r1)
    r2 = a - b
    print("Subtraction:")
    print(r2)
    r3 = a/b
    print("Division:")
    print(r3)
    r4 = a * b
    print("Multiplication:")
    print(r4)

#first array element raised to power fo second elements
def power():
    a = pd.Series([0 ,1, 2, 3, 4, 5, 6])
    b = np.array(a)
    print("Original Series:",b)
    c = np.power(b,3)
    print("Result:",c)

#diplay data in dataframe
def dataframe():
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    d = pd.DataFrame(exam_data, index = labels)
    print(d)

#accept user input options
io = input("1.array 2.list 3.math 4.power 5.dataframe Enter values:")

if io == "array":
    array()
elif io == "list":
    list()
elif io == "math":
    math()    
elif io == "power":
    power()
elif io == "dataframe":
    dataframe()
else: 
    print('Execute Success!!!')
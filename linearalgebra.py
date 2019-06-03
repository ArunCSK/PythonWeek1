
#sudo apt-get install python-pip python3-pip
#sudo pip3 install -U numpy
import numpy as np

#add two matrics
def add():
    x = [[12,7,3],[4 ,5,6],[7 ,8,9]]
    y = [[5,8,1],[6,7,3],[4,5,9]]
    result = [[0,0,0],[0,0,0],[0,0,0]]
    print(x, y)
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]
    
    for r in result:
        print(r)

#scaler multiplication
def scaler():
    x = [[12,7,3],[4,5,6],[7,8,9]]
    y = 9   
    result = [[0,0,0],[0,0,0],[0,0,0]]
    print("X = ", x)
    print("Y = ", y)
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] * y
    
    for r in result:
        print(r)

#multiply matrices and vector
def vector():
    x = [[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]]
    y = [1, 2, 3]
    result = [[0,0,0],[0,0,0],[0,0,0]]
    print("X = ",x)
    print("Y = ",y)
    for i in range(len(x)):
        for j in range(len(y)):
            result[j][i] = x[i][j] * y[i]

    for r in result:
        print(r)

#multiply matrices
def multiply():
    x = [[12,7,3],[4 ,5,6],[7 ,8,9]]
    y = [[5,8,1],[6,7,3],[4,5,9]]
    result = [[0,0,0],[0,0,0],[0,0,0]]
    print("X = ",x)
    print("Y = ",y)
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] * y[i][j]
    
    print("Result:")
    for r in result:
        print(r)

#inverse of matrices
def inverse():
    x = [[12,7,3],[4,5,6],[7 ,8,9]]
    print("X = ",x)
    y = np.linalg.inv(x)
    print("Inverse: ")
    print(y)
    #print(np.dot(x,y))


    

#accept user input options
io = input("1.add 2.scaler 3.vector 4.multiply 5.inverse Enter values:")

if io == "add":
    add()
elif io == "scaler":
    scaler()
elif io == "vector":
    vector()    
elif io == "multiply":
    multiply()
elif io == "inverse":
    inverse()
else: 
    print('Execute Succes!!!')
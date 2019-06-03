
import numpy as np

#convert array to 1d numpy array
def array():
    a1 = [12.23, 13.32, 100, 36.32]
    print("Original List: ",a1)
    print("One-dimenstional numpy array: ",np.array(a1))

#create matrix
def matrix():
    #m1 = [2 3 4 5 6 7]
    c = np.array([[2, 3, 4], [5,6,7], [8,9,10]])
    shape = (2, 10)
    print(c)

#create null vector and update 6th element
def vector():
    x = np.zeros(10)
    print("Null vector: ",x)
    x[6] = 11
    print("Updated: ",x)

#reverse an array
def reverse():
    a = np.arange(12,38)
    a1 = a[::-1]
    print(a)
    print(a1)

#2d array with 1 in the border and 0 inside
def border():
    a = np.ones((3,3))
    print("Orignail array:")
    print(a)
    print("result")
    a[1:-1, 1:-1] = 0
    print(a)

#accept user input options
io = input("1.array 2.matrix 3.vector 4.reverse 5.border Enter values:")

if io == "array":
    array()
elif io == "matrix":
    matrix()
elif io == "vector":
    vector()    
elif io == "reverse":
    reverse()
elif io == "border":
    border()
else: 
    print('Execute Success!!!')

import math 
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import seaborn as sb

#diplay random scatter plot file
def random():
    np.random.seed(19680801)
    N = 100
    r0 = 0.6
    x = 0.9 * np.random.rand(N)
    y = 0.9 * np.random.rand(N)
    area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
    c = np.sqrt(area)
    r = np.sqrt(x ** 2 + y ** 2)
    area1 = np.ma.masked_where(r < r0, area)
    area2 = np.ma.masked_where(r >= r0, area)
    plt.scatter(x, y, s=area1, marker='^', c=c)
    plt.scatter(x, y, s=area2, marker='o', c=c)
    # Show the boundary between the regions:
    theta = np.arange(0, np.pi / 2, 0.01)
    plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
    plt.show()

#diplay scatter plot with empty cricle
def circle():
    N = 500
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = (0,0,0)
    area = np.pi*3
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

#scater plot for camparission
def compare():
    math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
    science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
    marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    plt.scatter(marks_range,math_marks, label="maths")
    plt.scatter(marks_range,science_marks, label="science")
    plt.show()

#random ball distribution
def balls():
    no_of_balls = 25
    x = [np.random.randint(25) for i in range(no_of_balls)]
    y = [np.random.randint(25) for i in range(no_of_balls)]
    plt.scatter(x,y)
    plt.show()

#compare height and weights
def hw():
    weight1=[67,57.2,59.6,59.64,55.8,61.2,60.45,61,56.23,56]
    height1=[101.7,197.6,98.3,125.1,113.7,157.7,136,148.9,125.3,114.9] 
    weight2=[61.9,64,62.1,64.2,62.3,65.4,62.4,61.4,62.5,63.6]
    height2=[152.8,155.3,135.1,125.2,151.3,135,182.2,195.9,165.1,125.1] 
    weight3=[68.2,67.2,68.4,68.7,71,71.3,70.8,70,71.1,71.7]
    height3=[165.8,170.9,192.8,135.4,161.4,136.1,167.1,235.1,181.1,177.3]
    weight=np.concatenate((weight1,weight2,weight3))
    height=np.concatenate((height1,height2,height3))
    plt.scatter(weight, height, marker='*', color=['red','green','blue'])
    plt.xlabel('weight', fontsize=16)
    plt.ylabel('height', fontsize=16)
    plt.title('Group wise Weight vs Height scatter plot',fontsize=20)
    plt.show()

#accept user input options
io = input("1.random 2.circle 3.compare 4.balls 5.hw Enter values:")

if io == "random":
    random()
elif io == "circle":
    circle()
elif io == "compare":
    compare()   
elif io == "balls":
    balls()
elif io == "hw":
    hw()            
else: 
    print('Execute Success!!!')
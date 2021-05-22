import numpy as np
import pandas as pd

list = [1,2,3,4,5,5,6,6,4,3,2,4,5,4,6,78,8,9,88,66,44]

print('\n')
print("-------Using numpy------")
list = np.unique(list).tolist()
print(list)

print('\n')

print("-------Using pandas------")
list = pd.unique(list).tolist()
print(list)

from numpy.core.numeric import NaN
import pandas as pd
import numpy as np

# List of Tuples
employees = [('jack', 34, 'Sydney', 155),
            (NaN, 31, 'Delhi', 177.5),
            ('Aadi', NaN, 'Mumbai', 81),
            ('Mohit', 31, NaN, 167),
            ('Veena', 12, 'Delhi', 144),
            ('Shaunak', 35, 'Mumbai', NaN),
            ('Shaun', 35, 'Colombo', 111)
            ]

empDfObj = pd.DataFrame(employees, columns=['Name', 'Age', 'City', 'Marks'])

print(empDfObj)

dataTypeSeries = empDfObj.dtypes

print(dataTypeSeries)
#print(empDfObj.info)

print(empDfObj['Name'].isnull().values.any())

#empDfObj.loc[empDfObj['Name'].isnull(),'value_is_NaN'] = 'Arun'

if empDfObj["Name"].dtypes == 'object':
    empDfObj["Name"].fillna("Arun", inplace = True)

if empDfObj["Age"].dtypes == 'float64':
    empDfObj["Age"].fillna(((empDfObj["Age"].sum())/(empDfObj["Age"].count())).round(), inplace = True)
    empDfObj["Age"].astype(np.int64)

if empDfObj["City"].dtypes == 'object':
    empDfObj["City"].fillna('Delhi', inplace = True)

if empDfObj["Marks"].dtypes == 'float64':
    empDfObj["Marks"].fillna(35.50, inplace = True)

print(empDfObj)

import pandas as pd

df1 = pd.DataFrame(
        { 
            "A": ["A1", "A2", "A3"],
            "B": ["B1", "B2", "B3"],
            "C": ["A1", "C2", "C3"]
        },
        index= [0,1,2]
    )

df2 = pd.DataFrame(
        {   
            "A": ["D1", "D2", "D3"],
            "B": ["E1", "E2", "E3"],
            "C": ["F1", "F2", "F3"]
        },
        index= [4,5,6]
    )

# print("-------Using Join-----")
# print(df1.join(df2))
print("-------Using append-----")
print(df1.append(df2))
print("-------Using frames-----")
frames = [df1,df2]
print(pd.concat(frames))

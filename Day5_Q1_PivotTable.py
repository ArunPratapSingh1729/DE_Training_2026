import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie'] ,
    'Subject': ['Math', 'Math', 'Math'],
    'Score': [10,20,30]
}

df = pd.DataFrame(data)

df1  = pd.pivot_table(df , index = "Student" , values = ["Score"] , aggfunc = "max" )
print(df1)


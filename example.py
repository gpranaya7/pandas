import pandas as pd

#csv data to dataframe
pd.options.display.max_rows=72

df=pd.read_csv('text.csv')
print(df.to_string)

#dataframe

data={
'cars':['lamborghini','bmw','rangerover'],
       'origin':['italy','germany','uk']
 }
df=pd.DataFrame(data)
print(df)

#version
print(pd.__version__)

#series

l=[0,1,2]
res=pd.Series(l,index=['n1','n2'])
print(res)

#max_rows

print(pd.options.display.max_rows)


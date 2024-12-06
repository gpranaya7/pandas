import pandas as pd
df =pd.read_csv('text.csv')
#replacing wrong data using index
df.loc[2,'age']=20
print(df)

#replacing wrong data 
for person in df.index:
    if df.loc[person,'age']>100:
        df.drop(person,inplace=True)
print(df)

#removing duplicate data
print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df)
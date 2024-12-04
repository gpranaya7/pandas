import pandas as pd

#information about data

df=pd.read_csv('text.csv')
print(df.info())

#removing rows

df=pd.read_csv('text.csv')
df.dropna(inplace=True)
print(df)

#filling values

df.fillna(22,inplace=True)
print(df)

#filling values based on columns

df['age'].fillna(22,inplace=True)
print(df)

#mean,median,mode

val=df['age'].median()
df['age'].fillna(val,inplace=True)
print(df)

x=df['age'].mode()[0]
df['age'].fillna(x,inplace=True)
print(df)

n=df['age'].mean()
df['age'].fillna(n,inplace=True)
print(df)
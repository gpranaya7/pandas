import pandas as pd
df=pd.read_csv('text.csv')
df['date']=pd.to_datetime(df['date'],format='mixed')
df.dropna(subset='date',inplace=True)
print(df.to_string())

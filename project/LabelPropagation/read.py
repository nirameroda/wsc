import pandas as pd
data = pd.read_csv('./data/content1.csv')
print(data.iloc[:,-1:])
x= data.iloc[:,-1:]
#data['result'].values
print(x.result[1])
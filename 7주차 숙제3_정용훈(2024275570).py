import pandas as pd

data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age' :[20, 21, 19, 18]}
df = pd.DataFrame(data)
print(df)

from google.colab import drive
drive.mount('/content/gdrive')

csv_path = '/content/gdrive/My_Drive/Colab Notebooks/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

df.tail()

xlsx_path = '/content/gdrive/My_Drive/Colab Notebooks/TopSellingAlbums.xlsx'
df1 = pd.read_excel(xlsx_path)
df1.head()

x = df[['Genre']]
x
print(x)

x = df[['Artist']]
x
print(x)

y = df[['Artist', 'Length', 'Genre']]
y
print(y)

df.iloc[0, 0]
print(df.iloc[0,0])

df.iloc[1, 0]
print(df.iloc[1, 0])

df.iloc[0, 2]
print(df.iloc[0, 2])

df.loc[0, 'Artist']
print(df.loc[0, 'Artist'])

df.loc[0, 'Released']
print(df.loc[0, 'Released'])

df.loc[1, 'Released']
print(df.loc[1, 'Released'])

df.iloc[0:2, 0:3]
print(df.iloc[0:2, 0:3])

df.loc[0:2, 'Artist':'Released']

for i, j in df. iterrows():
    print(i, j)
    print()

filter2 = df["Claimed Sales (millions)"]>40

df.where(filter2)

#Quiz on DataFrame
q = df[['Rating']]
q
print(q)

q = df[['Released', 'Artist']]
q
print(q)

df.iloc[1, 2]
print(df.iloc[1, 2])
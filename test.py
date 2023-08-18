from util import load_df


df = load_df('data/GDP.csv', 'csv')
print(df.isnull().sum())
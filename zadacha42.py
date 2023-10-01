import pandas as pd
file_path = 'california_housing_train.csv'
df = pd.read_csv(file_path, sep=',')

print(df[df['population'] == df['population'].min()].households.max())
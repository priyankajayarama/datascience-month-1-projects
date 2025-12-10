import pandas as pd
df = pd.read_csv('/Users/priyankaj/Downloads/all_projects-2/project_week2/students_raw.csv')
df=df.drop_duplicates().dropna()
print(df.describe())
df.to_csv('students_cleaned.csv',index=False)

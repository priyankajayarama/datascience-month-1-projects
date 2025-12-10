import pandas as pd, numpy as np
s=pd.read_csv('/Users/priyankaj/Downloads/all_projects-2/project_week3/sales_data.csv')
s=s.dropna()
arr=np.array(s['sales'])
print('Total:',arr.sum())
print('Average:',arr.mean())
print('Best:',arr.max())
print('Worst:',arr.min())

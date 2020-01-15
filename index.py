import pandas as pd

data_p = pd.read_csv('in_data_p.csv', index_col='ad_id')
data_a = pd.read_csv('in_data_a.csv')

installs = data_a.query('installs > 0')

spend = data_p.query('spend > 0')

# new_df = pd.merge(spend, installs, how='inner')
# or(по умолчанию берется INNER)
new_df = spend.merge(installs)

new_df['cpi'] = new_df['spend'] / new_df['installs']

new_df.to_csv('out.csv', columns=['app', 'date', 'campaign', 'os', 'installs', 'spend', 'cpi'], index=False)

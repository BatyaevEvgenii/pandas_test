import pandas as pd


data_p = pd.read_csv('in_data_p.csv', index_col='ad_id')
data_a = pd.read_csv('in_data_a.csv', index='ad_id')


pd.options.display.float_format = '{:,.1f}'.format

# data_p.shape (19704, 3)
# data_p.columns Index(['date', 'campaign_id', 'spend'], dtype='object')
# data_p.dtypes
# date            object
# campaign_id      int64
# spend          float64
# dtype: object

# data_p.describe()
# data_p.head()
# data_p.sample()




installs = data_a.query('installs > 0 & ad_id == 33677384')
installs.groupby('id', 'date')['installs'].sum()

installs.groupby(['id', 'date', 'os', 'campaign', 'ad_id'])['installs'].sum()

installs.groupby(['id', 'date', 'os', 'campaign', 'ad_id'])['installs'].agg(['sum', 'count'])
installs.groupby(['id', 'date', 'os', 'campaign', 'ad_id'])['installs'].agg(['xxx'])


data_p.query('ad_id == 33677384')





# для id = 1190
spend = data_p.query('spend > 0 & ad_id == 33677384')
# spend.shape  (29, 3)
# spend.columns Index(['date', 'campaign_id', 'spend'], dtype='object')
# spend.index
# Int64Index([33677384, 33677384, 33677384, 33677384, 33677384, 33677384,
#             33677384, 33677384, 33677384, 33677384, 33677384, 33677384,
#             33677384, 33677384, 33677384, 33677384, 33677384, 33677384,
#             33677384, 33677384, 33677384, 33677384, 33677384, 33677384,
#             33677384, 33677384, 33677384, 33677384, 33677384],
#            dtype='int64', name='ad_id')







inst = data_a.query('Installs > 0 & id == 1190 & ad_id == 33677384')
inst.groupby(['id', 'date', 'os', 'campaign', 'ad_id'])['installs'].sum()
inst.shape
inst.columns


s_inst = inst.groupby(['id', 'date', 'os', 'campaign', 'ad_id'])['installs'].agg(['sum', 'count'])

s_spend = spend.groupby(['ad_id', 'date', 'spend'])['date'].agg(['sum', 'count'])


new_df = pd.merge(inst, spend,how='inner', left_index=True, right_on='ad_id')

new_df = pd.merge(installs, spend, how='inner', left_on='ad_id', right_index=True)
new_df = pd.merge(spend, installs, how='inner')
# or(по умолчанию берется INNER)
new_df = spend.merge(installs)
new_df['cpi']=new_df['spend'] / new_df['installs']
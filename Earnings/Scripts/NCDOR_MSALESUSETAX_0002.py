#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import requests


# In[ ]:


# Create backups
df_backup = pd.read_csv('./Updates/STG_BEA_MSALESUSETAX_0002.txt')
df_backup.to_csv('./Backups/STG_BEA_MSALESUSETAX_0002_BACKUP.txt')


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_10-18.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'Sales*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1', 'Sales*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'Sales*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'Sales*.1':'Sales'})

# append2 dataframes
df_append2 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append2 = df_append2.dropna(how='all')
df_append2 = df_append2.fillna('0')

# Change dtypes to Int
df_append2['Sales'] = df_append2['Sales'].astype(float)

# Drop junk rows
df_append2 = df_append2[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_11-18.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'Collections*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1', 'Sales*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'Sales*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'Collections*.1':'Sales'})

# append3 dataframes
df_append3 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append3 = df_append3.dropna(how='all')
df_append3 = df_append3.fillna('0')

# Change dtypes to Int
df_append3['Sales'] = df_append3['Sales'].astype(float)

# Drop junk rows
df_append3 = df_append3[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_12-18.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'Collections*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1', 'Sales*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'Sales*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'Collections*.1':'Sales'})

# append4 dataframes
df_append4 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append4 = df_append4.dropna(how='all')
df_append4 = df_append4.fillna('0')

# Change dtypes to Int
df_append4['Sales'] = df_append4['Sales'].astype(float)

# Drop junk rows
df_append4 = df_append4[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_1-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append5 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append5 = df_append5.dropna(how='all')
df_append5 = df_append5.fillna('0')

# Change dtypes to Int
df_append5['Sales'] = df_append5['Sales'].astype(float)

# Drop junk rows
df_append5 = df_append5[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_2-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append = df_append.dropna(how='all')
df_append = df_append.fillna('0')

# Change dtypes to Int
df_append['Sales'] = df_append['Sales'].astype(float) 

# Drop junk rows
df_append = df_append[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_3-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append6 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append6 = df_append6.dropna(how='all')
df_append6 = df_append6.fillna('0')

# Change dtypes to Int
df_append6['Sales'] = df_append6['Sales'].astype(float) 

# Drop junk rows
df_append6 = df_append6[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_4-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append7 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append7 = df_append7.dropna(how='all')
df_append7 = df_append7.fillna('0')

# Change dtypes to Int
df_append7['Sales'] = df_append7['Sales'].astype(float)
 

# Drop junk rows
df_append7 = df_append7[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_5-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append8 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append8 = df_append8.dropna(how='all')
df_append8 = df_append8.fillna('0')

# Change dtypes to Int
df_append8['Sales'] = df_append8['Sales'].astype(float)
 

# Drop junk rows
df_append8 = df_append8[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_6-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append9 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append9 = df_append9.dropna(how='all')
df_append9 = df_append9.fillna('0')

# Change dtypes to Int
df_append9['Sales'] = df_append9['Sales'].astype(float)
 

# Drop junk rows
df_append9 = df_append9[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_7-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append10 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append10 = df_append10.dropna(how='all')
df_append10 = df_append10.fillna('0')

# Change dtypes to Int
df_append10['Sales'] = df_append10['Sales'].astype(float)
 

# Drop junk rows
df_append10 = df_append10[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_8-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append11 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append11 = df_append11.dropna(how='all')
df_append11 = df_append11.fillna('0')

# Change dtypes to Int
df_append11['Sales'] = df_append11['Sales'].astype(float)
  

# Drop junk rows
df_append11 = df_append11[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_9-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append12 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append12 = df_append12.dropna(how='all')
df_append12 = df_append12.fillna('0')

# Change dtypes to Int
df_append12['Sales'] = df_append12['Sales'].astype(float)
 

# Drop junk rows
df_append12 = df_append12[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_10-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append13 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append13 = df_append13.dropna(how='all')
df_append13 = df_append13.fillna('0')

# Change dtypes to Int
df_append13['Sales'] = df_append13['Sales'].astype(float)
 

# Drop junk rows
df_append13 = df_append13[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_11-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append14 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append14 = df_append14.dropna(how='all')
df_append14 = df_append14.fillna('0')

# Change dtypes to Int
df_append14['Sales'] = df_append14['Sales'].astype(float)
 

# Drop junk rows
df_append14 = df_append14[:-5]


# In[ ]:


# Read excel file
df = pd.read_excel('https://files.nc.gov/ncdor/documents/reports/monthly_sales_12-19.xls', skiprows = 9)

# Drop NaN row
df = df.drop(df.index[0])
df = df[:-8]

# Remove columns with amiguous names
df = df.loc[:,~df.columns.str.contains('Unnamed')]

# Create new dataframe with second set of counties
df2 = pd.DataFrame(df, columns = ['County.1', 'and Purchases*.1'])

# Drop second set of counties from original dataframe
df = df.drop(columns=['County.1', 'Collections*', 'Collections*.1','and Purchases*.1'])

# Rename columns
df = df.rename(columns = {'County.1':'County', 'and Purchases*':'Sales'})
df2 = df2.rename(columns = {'County.1':'County', 'and Purchases*.1':'Sales'})

# Append dataframes
df_append15 = df.append(df2, ignore_index=True)

# Drop rows that are all NaN and replace NaN with 0 if the entire row is not NaN
df_append15 = df_append15.dropna(how='all')
df_append15 = df_append15.fillna('0')

# Change dtypes to Int
df_append15['Sales'] = df_append15['Sales'].astype(float)
 

# Drop junk rows
df_append15 = df_append15[:-5]


# In[ ]:


df_master = pd.concat([df_append, df_append2, df_append3, df_append4, df_append5, df_append6, df_append7, df_append8,
                       df_append9, df_append10, df_append11, df_append12, df_append13, df_append14, df_append15])
print(df_master.shape[0])
print(df_master.shape[1])


# In[ ]:


df_master = df_master.sort_values(by = 'County', ascending=True)
df_master['Sales'] = df_master['Sales'].round(0)
df_master = df_master.set_index('County')
df_master.head(20)


# In[ ]:


df_master = df_master.to_csv('./Updates/STG_BEA_MSALESUSETAX_0002.txt', sep='\t')

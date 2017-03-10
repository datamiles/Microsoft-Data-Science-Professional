import pandas as pd
import html5lib

# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
table_dataframe= pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]
#print type(table_dataframe)
#print table_dataframe
# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
# .. your code here ..
df = table_dataframe.drop([0,1])
df.head()
df.columns = ['RK','PLAYER','TEAM','GP','G','A','PTS','+/-',
                           'PIM','PTS/G','SOG','PCT','CWG','PPG','PPA','SHG','SHA']

df = df.drop(12, axis=0)
df = df.drop(24, axis=0)
df = df.drop(36, axis=0)
df = df.drop(13, axis=0)
df = df.drop(25, axis=0)
df = df.drop(37, axis=0)
      
df = df.drop(["RK"], axis=1)
                     
df.head()

# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
# .. your code here ..


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..


# TODO: Get rid of the 'RK' column
#
# .. your code here ..


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reset_index(drop=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..
df.dtypes
df.head()

# array of column name and change type in a for loop
df_columns = ['GP','G','A','PTS','+/-']
print df_columns

for i in df_columns:
    #df.[i] = pd.to_numeric(df.[i], errors='coerce')
    df.loc[:,i] = pd.to_numeric(df.loc[:,i], errors='coerce')
    print i

for column in df:
    print(df[column])

df.GP = pd.to_numeric(df.GP, errors='coerce')
df.G = pd.to_numeric(df.G, errors='coerce')
df.A = pd.to_numeric(df.A, errors='coerce')
df.PTS = pd.to_numeric(df.PTS, errors='coerce')

df.loc[:,'+/-'] = pd.to_numeric(df.loc[:, '+/-'], errors='coerce')

df.PIM = pd.to_numeric(df.PIM, errors='coerce')
df.loc[:,'PTS/G'] = pd.to_numeric(df.loc[:, 'PTS/G'], errors='coerce')

df.SOG = pd.to_numeric(df.SOG, errors='coerce')

df.PCT = pd.to_numeric(df.PCT, errors='coerce')
df.CWG = pd.to_numeric(df.CWG, errors='coerce')
df.PPG = pd.to_numeric(df.PPG, errors='coerce')
df.PPA = pd.to_numeric(df.PPA, errors='coerce')
df.SHG = pd.to_numeric(df.SHG, errors='coerce')
df.SHA = pd.to_numeric(df.SHA, errors='coerce')

df.dtypes
df.head()

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..
unique_pct = df.PCT.unique()
len(unique_pct)

df.loc[15:16, 'GP'].sum()
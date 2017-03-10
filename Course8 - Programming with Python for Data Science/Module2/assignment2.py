import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..
datafile = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module2\\Datasets\\tutorial.csv'
df = pd.read_csv(datafile)


# TODO: Print the results of the .describe() method
#
# .. your code here ..
df.describe()


# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
df.col3
df['col3']
df.loc[:'col3']
df.loc[:,'col3']
df.loc[2:4,'col3']
df.iloc[2:4,[3]]
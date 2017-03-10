import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
datafile = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module2\\Datasets\\servo.data'
df = pd.read_csv(datafile, names=['motor', 'screw', 'pgain', 'vgain', 'class'])

df.head()

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
vgain_uniques = df.vgain.unique()
print vgain_uniques
vgain_vcounts = df.vgain.value_counts()
print vgain_vcounts
vgain5_slice = df[df['vgain']==5]
len(vgain5_slice)

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
m_s_e_slice = df[(df['motor']=='E') & (df['screw']=='E')]
print len(m_s_e_slice)

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
pgain_4_slice = df[df['pgain']==4]
print pgain_4_slice
mean_vg_pg_4 = pgain_4_slice.vgain.mean()
print mean_vg_pg_4
# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
df.dtypes



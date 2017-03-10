# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 14:59:35 2017

@author: snasir
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot') # Look Pretty
# If the above line throws an error, use plt.style.use('ggplot') instead
from mpl_toolkits.mplot3d import Axes3D

datafile = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module3\\Datasets\\students.data'
df = pd.read_csv(datafile)
df.head()

students_data = pd.read_csv(datafile, index_col=0)
students_data.head()

my_series = students_data.G3
my_df = students_data[['G3','G2','G1']]

my_series.plot.hist(alpha=0.5)
my_df.plot.hist(alpha=0.5)


wheat_datafile = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module3\\Datasets\\wheat.data'
wheat_data = pd.read_csv(wheat_datafile)
wheat_data.head()

wheat_data.asymmetry.plot.hist(title='Asymmetry', bins=6)
plt.show()

wheat_data.asymmetry.plot.hist(title='Asymmetry', bins=10)
plt.show()

print(wheat_data.wheat_type.unique())

wheat_data['wheat_type'] = wheat_data.wheat_type.astype("category").cat.codes
print(wheat_data.wheat_type.unique())

# Map column values for wheat type from 1 0 2 to 3 2 1
wheat_dict = {1:2, 2:3, 0:1}

wheat_data["wheat_type"].replace(wheat_dict, inplace=True)

print(wheat_data.wheat_type.unique())

plt.figure()
wheat_data[wheat_data.wheat_type==3].asymmetry.plot.hist(alpha=0.3)
wheat_data[wheat_data.wheat_type==2].asymmetry.plot.hist(alpha=0.6)
wheat_data[wheat_data.wheat_type==1].asymmetry.plot.hist(alpha=0.6)
plt.show()


# Scatter plots
students_data.plot.scatter(x='G1', y='G3')

# 3D scatter plots
fig= plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Alcohol Use')

ax.scatter(students_data.G1, students_data.G3, students_data['Dalc'], c='r', marker='.')
plt.show()
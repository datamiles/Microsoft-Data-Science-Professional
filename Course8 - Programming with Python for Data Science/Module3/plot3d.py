# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 16:22:42 2017

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

fig= plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Alcohol Use')

ax.scatter(students_data.G1, students_data.G3, students_data['Dalc'], c='r', marker='.')
plt.show()


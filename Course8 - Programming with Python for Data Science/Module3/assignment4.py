import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
wheat_datafile = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module3\\Datasets\\wheat.data'
wheat_data = pd.read_csv(wheat_datafile)
wheat_data.head()


#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features
# 
# .. your code here ..
# axis 0 is rows
# axis 1 is columns

# dropping a column using axis=1
wheat_data = wheat_data.drop(["id","area","perimeter"], axis=1)
wheat_data.head()

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..

plt.figure()
parallel_coordinates(wheat_data, 'wheat_type')

plt.show()



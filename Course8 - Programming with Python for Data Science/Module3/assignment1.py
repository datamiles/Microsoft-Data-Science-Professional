import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

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
# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
# 
# .. your code here ..
s1 = wheat_data[['area','perimeter']]
s1.head()
#
# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
# 
# .. your code here ..
s2 = wheat_data[['groove','asymmetry']]
s2.head()

#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
# 
# .. your code here ..
s1.plot.hist(alpha=0.75)
s2.plot.hist(alpha=0.75)
# Display the graphs:
plt.show()


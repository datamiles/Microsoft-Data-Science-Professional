# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:51:11 2017

@author: snasir
"""

import pandas as pd

datafile = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module2\\Datasets\\tutorial.csv'
df = pd.read_csv(datafile)

df.head()
df.tail()
df.describe()
df.columns

headers = ['one','two','three','four']
datafile2 = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module2\\Datasets\\tutorialnoheaders.csv'
df = pd.read_csv(datafile2, names=headers)

print df
df

df.columns=['o','t','th','f']

# axis 0 is rows
# axis 1 is columns

# dropping a column using axis=1
df = df.drop(["f"], axis=1)

# dropping row using axis=0
df = df.drop(3, axis=0)

# column data types
df.dtypes

"""
Slicing and Dicing 
Part One - Slicing
Series and Data Frames
"""
datafile = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module2\\Datasets\\direct_marketing.csv'
df = pd.read_csv(datafile)
df.head()

# Step 1 - Indexing
df.recency
df['recency']
df[['recency']]
df.loc[:,'recency']

# Slicing by a list parameter will return a data frame opposed to a series
# df[['recency']], df.loc[:, ['recency']], and df.iloc[:, [0]]

#
# Produces a series object:
df.recency
df['recency']
df.loc[:, 'recency']
df.iloc[:, 0]
df.ix[:, 0]

#
# Produces a dataframe object:
df[['recency']]
df.loc[:, ['recency']]
df.iloc[:, [0]]

# column and row indexer
# loc and ix are inclusive
# iloc is non-inclusive

df[0:2]
df.iloc[0:2,1:3]
df.loc[0:4, ['history', 'visit']]

"""
Slicing and Dicing
Part two - Dicing
"""

# Boolean Indexing
df.recency < 7

# Indexing Boolean Series
df[df.recency < 7]

# Fine grain boolean indexing
df[(df.recency<7) & (df.newbie==0)]

df[df.recency <7][0:2]   
df[df.recency <7] = -100
df



"""
Feature Representation
"""

# Textual Categorical Features - Ordinal or Nominal

# Assigning order to category - example 1
ordered_day_type = ['hot','mild','wet','cold']
df = pd.DataFrame({'day':['muggy','hot','mild','wet','cold']} )
df.day = df.day.astype("category",
                       ordered=True,
                       categories = ordered_day_type).cat.codes
df

# Assigning order to category - example 2
# astype maps the unfound value to -1
ordered_satisfaction = ['Very Unhappy', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']
df = pd.DataFrame({'satisfaction':['Mad', 'Happy', 'Unhappy', 'Neutral']})
df.satisfaction = df.satisfaction.astype("category",ordered=True,categories = ordered_satisfaction).cat.codes
#df.satisfaction = df.satisfaction.astype("category",ordered=True,categories=ordered_satisfaction).cat.codes
df

ordered_satisfaction = ['Very Unhappy', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']
df = pd.DataFrame({'satisfaction':['Mad', 'Happy', 'Unhappy', 'Neutral']})
df.satisfaction = df.satisfaction.astype("category",
  ordered=True,
  categories=ordered_satisfaction
).cat.codes
df

# Two approaches for the nominal category series
# Method 1
# Order just based on astype("category") like ordinal
# pandas alphabetically orders the data
df = pd.DataFrame({'vertebrates': ['Bird',
                                   'Bird',
                                   'Mammal',
                                   'Fish',
                                   'Amphibian',
                                   'Reptile',
                                   'Mammal']})
print df
df['vertebrates'] = df.vertebrates.astype("category").cat.codes
print df
df['vertebrates'] = df.vertebrates.astype("category").cat.codes
df

df = pd.DataFrame({'vertebrates':[
 'Bird',
 'Bird',
 'Mammal',
 'Fish',
 'Amphibian',
 'Reptile',
 'Mammal',
]})

# problem with method 1 is that values assigned are increasing in an order
# however there is no order between the values 

# Method 1)
df['v'] = df.vertebrates.astype("category").cat.codes

df


# Method 2
# get_dummies method allows replacing a nominal feature with multiple boolean features
# benefit: no erroneous ordering is introduced in the dataset
# get_dummies helps destroys the implicit relationship that was introduced by method 1
# start with method 1 and use method 2 if necessary
# Method 1 is basically converting feature in to discrete feature
# whereas method 2 is exploding the feature into a set of new boolean features

df = pd.get_dummies(df,columns=['vertebrates'])
df



"""
Textual Features
"""
# turning written text into a feature
# you can do classification or clustering on the text among other options
# scikit learn implements bag-of-words method for featurizing text
# using this method every word becomes a feature
# each feature is a count of how many times a word occurs
# bag of words implementation requires CountVectorizer method in scitkit learn

from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Osman ran faster than Jul because he is an athlete.",
          "Osman and Jul ran faster and faster an yea"]
          
bow = CountVectorizer()
X = bow.fit_transform(corpus)

bow.get_feature_names()
print bow.get_feature_names()
# featurizing a text can result in a very large array
# so in order to save space and memory complexity scikit saves the output as sparse matrix
# you can convert it to python list by using toarray method
print X.toarray()

# count vertorizer can be used to ignore frequently used words like the, such etc
# you can also strip accents and punctuations
# you can have it work on characters instead of words
# or pair of words
# you can provide your own tokenizer

# how do you featurize an image?
# one way is to read every single pixel of the image as a one dimensional feature array
# with the pixel luminsity being the value thats actually recorded
# you are losing some intrinsic info such as two dimensional arrangement of the picture
# however granted the number of pixels an average image has - even a small one
# good ML results can be obtained

# using scipy to read in the image file
from scipy import misc
image = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module2\\DSC_0048.JPG'
img = misc.imread(image)
img = img[::2, ::2]
X = (img/255.0).reshape(-1)
print X

# :: is called extended slicing
# reshape(-1) tells pandas to take 2D image and flatten it to 1D array
# another method ravel will do the same thing as reshape(-1)
# reason it is necessary to reshapre 2D array images into one dimensional ones is because
# each image will represent a single sample and SKLearn expects your data frame
# to be shapes [num_samples, num_features]

# Grayscale
red = img[:,0]
green = img[:,1]
blue = img[:,2]

gray = (0.299*red + 0.587*green+ 0.114*blue)

print img.shape
print gray.shape


"""
Wrangling Your Data
"""
# Data could be missing, or contain bad data points
# These data points should be dealt with
# Pandas represent missing data using Numpy's np.nan 
# nan works differently from Python's NONE keyword
# so in order to test for it you will have use two of pandas testing functions
# isnull or notnull
# these methods work on both series and data frame and return bolean array
# that can be filtered further

# Method 1 to get rid of nans
# completely fill each data point in the data frame or the series with a scalar value
datafile = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module2\\Datasets\\direct_marketing.csv'
df = pd.read_csv(datafile)

print df.columns

print df.zip_code.isnull()
print df.notnull()

len(df)
df = df.drop_duplicates(subset=['zip_code']).reset_index()
len(df)

# you can also forward fill and interpolate data
# drop = true tells pandas to not keep a backup copy of original index
df = df.reset_index(drop=True)

datafile = 'C:\\Users\\snasir\\DAT210x-master\\DAT210x-master\\Module2\\Datasets\\direct_marketing.csv'
df = pd.read_csv(datafile)

df.zip_code.unique()
df.visit.value_counts()

df.dtypes
df

df.visit[df.visit==0] = 1
df
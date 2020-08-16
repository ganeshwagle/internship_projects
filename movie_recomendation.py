#import all the required libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('movies_150.csv')
print(df)

#creating the list of important columns for the recomendation engine
columns = ['actors','director','genre','title']
df[columns].head(3)

#checking if there any null values
if df[columns].isnull().values.any():
  df = df.fillna(' ')
else:
  print('none')
  
#function to combine the values of the important columns into a single string
def get_important_features(data):
  features = []
  for i in range(0,data.shape[0]):
    features.append(data['actors'][i]+data['director'][i]+data['genre'][i]+data['title'][i])
  return features

#creat a column to hold the combined string
df['imp features'] = get_important_features(df)
df.head()

#convert the text to matrix of token count
cm = CountVectorizer().fit_transform(df['imp features'])

#Get the cosine similarity matrix from the count matrix
cs = cosine_similarity(cm)
#print the cosine similarity matrix
print(cs)

#get the title of the movie
Title = input('Enter the name of the movie:')
Title = Title.lower()
df['title'] = df['title'].str.lower()
if Title not in list(df['title']):
  print('That movie is not there in the data set')
  exit()
else:
  #get the index of the movie
  index = df[df['title']==Title].index.values[0]
  print(index)


#creat a list of enumeration for the similarity score [(index, similarity score),...]
scores = list(enumerate(cs[index]))
print(scores)

#sort the list here in lamda function it is x:x[1] because x is score and x[1] will give similarity score 
sorted_score = sorted(scores, key = lambda x:x[1],reverse=True)
print(sorted_score)
sorted_score = sorted_score[1:]
#since the first movie is the movie which the user entered

#print the top ten recomended movies
#get the index of the title column
columns = df.columns
title_index = columns.get_loc('title')
j = 0
for item in sorted_score:
  name = df.iloc[item[0],title_index]
  print(j+1,name)
  j = j+1
  if j>9:
    break

#this is stock price prediction using machine learning
#importing all the required libraries
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer 
from sklearn.svm import SVR
import joblib

#creating the dataframe
df = pd.read_csv('D:\internship\Reliance.csv')
print(df.head())

#We only need closing price to predict the stock price so I'm gonna plot only that one
plt.figure(figsize=(16,8))
plt.title('Reliance')
plt.xlabel('Days')
plt.plot(df['Close'])
plt.show()

#Creating dependent and independent variables
#Our target variable is stock price we going to predict the stock price of the share in the future using stock price in the past 
#So what we need to so is crate another column which contains the stock price after 'n' days

future_days = 25

#The independent variable will contain all the close price except the the last 'n' rows 
#the reason being we are creating the target variable by shifting the close price by 'n' days so infont of todays closing price there will be
#the closing price of the share after 'n' days
df= df[['Close']]
df['Prediction'] = df[['Close']].shift(-future_days)
print(df)

#creating dependent and independent variable
x = np.array(df.drop(['Prediction'],1))
#remove last 'n' rows
x = x[:-future_days]
y = np.array(df.drop(['Close'],1))
y = y[:-future_days]
#removing all the nan values
simp = SimpleImputer()
x[:,:] = simp.fit_transform(x[:,:])
y[:,:] = simp.fit_transform(y[:,:])

#spliting the data sets
x_train,x_test,y_train,y_test = tts(x,y,test_size = .25, random_state = 43)

#Using linear regression model
linreg = LinearRegression()
linreg.fit(x_train,y_train)
print(linreg.score(x_train, y_train))

linregpred=linreg.predict(x_test)
print(linreg.score(x_test, y_test))
plt.scatter(y_test,linregpred)

#using svm model to predict the stock price
svr = SVR(C = 1e2, gamma = 0.001)
svr.fit(x_train, y_train.ravel())
print(svr.score(x_train, y_train))

svrpred=svr.predict(x_test)
print(svr.score(x_test, y_test))
plt.scatter(y_test,svrpred)

#saving linear regression model
joblib.dump(linreg,'linreg.sav')
loadmodel1=joblib.load('linreg.sav')
print(loadmodel1.score(x_test,y_test))

#saving support vector
joblib.dump(svr,'svm.sav')
loadmodel2=joblib.load('svm.sav')
print(loadmodel2.score(x_test,y_test))
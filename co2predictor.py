import numpy as np
import pandas as pd
import warnings
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import requests

def cum(year_num):
  response = requests.get('https://github.com/ColinJ69/Co2Awareness/raw/main/Book%202%20(1).xlsx')
  data = pd.read_excel(response.content, usecols=[0,1])
  x = np.array(data['Year'])
  y = np.array(data['Tonnes'])
  X = x.reshape(-1,1)
  reg = LinearRegression().fit(X,y)
  year_arr =  np.array(year_num)
  return int(f'{reg.predict(input_arr.reshape(1,-1))} tonnes in year_num)

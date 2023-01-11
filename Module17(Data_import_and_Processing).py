import urllib.request
import pandas as pd

urllib.request.urlretrieve(
    "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    , "C:/Users/15/Desktop/DataSet/[Dataset]_Module_17_iris.data"
)#url에서 iris데이터를 받아 지정된 경로에 저장

df = pd.read_csv('C:/Users/15/Desktop/DataSet/[Dataset]_Module_17_iris.data')
print(df.head())

df = pd.read_csv("C:/Users/15/Desktop/DataSet/[Dataset]_Module_17_Iris.data",header=None)
print(df.head())

names = ["sepal_length", "sepal_width","petal_length", "petal_width", "class"]
df.columns = names
print(df.head())# 만약 csv파일에 컬럼명이 없는 경우 사용 방법

print(df.info())
print(df.describe())

import pandas as pd
import numpy as np

def standarddeviation():
    Location ="datasets/gradedata.csv"
    df = pd.read_csv(Location)
    # mean value
    meangrade = df['grade'].mean()
    # standard deviation
    stdgrade =df['grade'].std()
    # top limit value
    toprange = meangrade + stdgrade * 1.96
    botrange = meangrade - stdgrade * 1.96
    copydf = df
    print(copydf.size)
    # we remove the element with values > toprange, remove with index
    copydf = copydf.drop(copydf[copydf['grade'] > toprange].index)
    copydf = copydf.drop(copydf[copydf['grade'] < botrange].index)
    print(copydf.size)

# Interquartile Range (IQR) : IQR is the difference between the 25 % and 75% percent quantile

def interquartileRange():
    Location = "datasets/gradedata.csv"
    df = pd.read_csv(Location)
    q1 = df['grade'].quantile(0.25)
    q3 = df['grade'].quantile(0.75)
    iqr = q3-q1
    toprange = q3+iqr*1.5
    botrange = q3-iqr*1.5
    copydf = df
    print(copydf.size)
    # we remove the element with values > toprange, remove with index
    copydf = copydf.drop(copydf[copydf['grade'] > toprange].index)
    copydf = copydf.drop(copydf[copydf['grade'] < botrange].index)
    print(copydf.size)

def missingdata():
    df = pd.read_csv("datasets/gradedata.csv")
    print(df.head())
    # drop rows with missing data
    df_no_missing = df.dropna()
    # add columln filled qith emtpy values
    df['newcol'] = np.nan
    print(df.head())
    # drop all empty values
    df.dropna(axis=1,how='all')
    # replace empty cells with zero
    df.fillna(0)
    # replace missing values with mean values
    df["grade"].fillna(df["grade"].mean(),inplace=True)
    # replace with gender values
    df["grade"].fillna(df.groupby("gender")["grade"].transform("mean"),inplace=True)
    #selecting rows with no missing Age ou Gender
    df[df['age'].notnull() & df['gender'.notnull()]]

def filteringvalues():
    names =['Bob','Jessica','Mary','John','Mel']
    grades = [76,-2,77,78,101]

    GradeList = list(zip(names,grades))
    df = pd.DataFrame(data=GradeList, columns=['Names','Grades'])
    print(df)
    print(df.loc[df['Grades']<=100])
    # renvoie un boolean pour indiquer si rempli la condition
    print((df['Grades'] >= 100,'Grades'))
    df.loc[(df['Grades'] >= 100,'Grades')]=100
    print(df)


standarddeviation();
interquartileRange();
filteringvalues()
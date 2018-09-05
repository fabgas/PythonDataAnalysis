import pandas as pd
import numpy as np
import string
from time import strftime
from datetime import datetime

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

def findingDuplicateRows():
    names =['Jan','John','Bob','Jan','Mary','Jon','Mel','Mel']
    grades = [95,78,76,95,77,78,99,100]
    GradeList = list(zip(names,grades))
    df = pd.DataFrame(data = GradeList,
                      columns=['Names','Grades'])
    print(df)
    #print only the duplicate rows
    print(df.duplicated())
    #print df without the duplicate rows
    print(df.drop_duplicates())

exclude = set(string.punctuation)
def remove_punctuation(x):
    try:
        x = ''.join(ch for ch in x if ch not in exclude)
    except:
        pass
    return x

def remove_whitespace(x):
    try:
        x = ''.join(x.split())
    except:
        pass
    return x




def removePunctuationFromColumncontent():
    Location = "datasets/gradedata.csv"
    ## to add headers as we load the data...
    df = pd.read_csv(Location)
    print(df.head())
    df.address = df.address.apply(remove_punctuation)
    print(df)
    df.address = df.address.apply(remove_whitespace)
    print(df)

def standardize_date(thedate):
    formatted_date =""
    thedate = str(thedate)
    if not thedate or thedate.lower() =="missing" or thedate == "nan":
        formatted_date = "MISSING"
    if thedate.lower().find('x') != -1:
        formatted_date="Incomplete"
    if thedate[0:2] == "00":
        formatted_date = thedate.replace('00','19')
    try:
        formatted_date = str(datetime.strptime(thedate,'%m/%d/%y').strftime('%m/%d/%y'))
    except:
        pass
    try:
        formatted_date= str(datetime.strptime(thedate,'%m/%d/%y'))
    except:
        pass
    try:
        if int(thedate[0:4]) < 1900:
            formatted_date = 'Incomplete'
        else:
            formatted_date = str(datetime.strptime(thedate,'%Y-%m-%d').strftime('%m/%d/%y'))
    except:
        pass
    return formatted_date;

def standard_date():
    names =['Bob','Jessica','Mary','John','Mel']
    grades = [76,99,77,78,99]
    bsdegrees = [1,1,0,0,1]
    msdegrees = [2,1,0,0,0]
    phddegrees = [0,1,0,0,0]
    bdates = ['1/1/1945','10/21/76','3/3/90','04/30/1901','1963-09-01']
    GradeList = list(zip(names,grades,bsdegrees,msdegrees,phddegrees,bdates))
    columns= ['Names','Grades','BS','MS','PhD','bdates']
    df = pd.DataFrame(data = GradeList,columns=columns)
    print(df)
    df.bdates = df.bdates.apply(standardize_date)
    print(df)

#standarddeviation();
#interquartileRange();
#filteringvalues();
#findingDuplicateRows();
#removePunctuationFromColumncontent();
standard_date();
import pandas as pd
import numpy as np
from numpy import random
from numpy.random import randint
import glob
from sqlalchemy import create_engine
import os
import sqlite3 as lite

def load_simple():
    #load a csv and print the first five lines
    location ="datasets/smallgradesh.csv"
    df = pd.read_csv(location,header=None)
    print(df.head())

def load_add_header():
    # load a csv and add a header
    location = "datasets/smallgrades.csv"
    # to add headers as we load the data
    df = pd.read_csv(location,names=['Names','Grades'])
    # to add headers to a dataframe
    df.columns = ['Names','Grades']

def save_data_csv():
    names = ['Bob','Jessica','Mary','John','Mel']
    grades = [76,95,77,78,99]
    #in python 3, should use list because zip return an iterator
    GradeList = list(zip(names,grades))
    df = pd.DataFrame(data = GradeList,columns=['Names','Grades'])
    df.to_csv('datasets/studentgrades.csv',index=False,header=False)

def load_data_excel():
    Location = "datasets/gradedata.xlsx"
    df = pd.read_excel(Location)
    print(df.head())
    #change columns names
    df.columns = ['first','last','sex','age','exer','hrs','grd','addr']
    print(df.head)

def save_data_excel():
    names = ['Bob','Jessica','Mary','John','Mel']
    grades = [76,95,77,78,99]
    GradeList = list(zip(names,grades))
    df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
    writer = pd.ExcelWriter('datasets/dataframe.xlsx',engine='xlsxwriter')
    df.to_excel(writer,sheet_name='Sheet1')
    writer.save()

def multiples_file_same_dataframe():
    all_data = pd.DataFrame()
    df = pd.read_excel("datasets/data1.xlsx")
    all_data = all_data.append(df,ignore_index=True)
    df = pd.read_excel("datasets/data2.xlsx")
    all_data = all_data.append(df,ignore_index=True)
    df = pd.read_excel("datasets/data3.xlsx")
    all_data = all_data.append(df,ignore_index=True)
    print(all_data.describe())

def multiple_file_scale():
    all_data = pd.DataFrame();
    for f in glob.glob("datasets/data*.xlsx"):
        df = pd.read_excel(f)
        all_data = all_data.append(df,ignore_index=True)
    print(all_data.describe())

# execute a request in a database
def load_data_sql():
    # connect to sqlite db
    db_file = r'datasets/gradedata.db'
    engine = create_engine(r"sqlite:///{}".format(db_file))
    sql = 'SELECT * from test where Grades in (76,77,78)'
    sales_data_df = pd.read_sql(sql,engine)
    print(sales_data_df)

# gives all the table in the sql database
def list_tables():
    # connect to sqlite db
    db_file = r'datasets/gradedata.db'
    engine = create_engine(r"sqlite:///{}".format(db_file))
    sql = "select name from sqlite_master where type ='table';"
    print(pd.read_sql(sql,engine))

def save_data_to_sql():
    # create the dataset to save
    names = ['Bob','Jessica','Mary','John','Mel']
    grades = [76,95,77,78,99]
    GradeList = list(zip(names,grades))
    df = pd.DataFrame(data = GradeList,columns=['Names','Grades'])
    print(df)
    db_filename = r'datasets/mydb.db'
    con = lite.connect(db_filename)
    # flavor disappears
    df.to_sql('mytable',
              con,
              schema=None,
              if_exists='replace',
              index=True,
              index_label=None,
              chunksize=None,
              dtype=None)
    con.close()

def random_generation():
    names = ['Bob','Jessica','Mary','John','Mel']
    random.seed(500)
    randnames = []
    for i in range(1000):
        name = names[randint(low=0,high=len(names))]
        randnames.append(name)
    births = []
    for i in range(1000):
        births.append(randint(low=0,high=1000))

    BabyDataSet2 = list(zip(randnames,births))
    df = pd.DataFrame(data = BabyDataSet2, columns=['Names','Births'])
    print(df)

load_simple();
load_add_header();
save_data_csv();
load_data_excel();
save_data_excel();
multiples_file_same_dataframe();
multiple_file_scale();
load_data_sql();
list_tables();
save_data_to_sql();
random_generation();
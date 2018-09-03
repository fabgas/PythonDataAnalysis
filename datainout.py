import pandas as pd

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

load_simple();
load_add_header();
save_data_csv();
load_data_excel();
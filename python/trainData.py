import csv
import pandas as pd 

def returnHeader(cfile): 
    with open(cfile, newline='') as f: 
        c_reader = csv.reader(f)
        return next(c_reader)


def return_xlabels(cfile, features): 
    df = pd.read_csv(cfile)
    t = []
    for item in features: 
        t.append(df[item].values)
    return t


def return_ylabels(cfile, ycol):
    df = pd.read_csv(cfile)
    return df[ycol].values


# print(return_ylabels("AAPL.csv", "High"))

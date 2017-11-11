import pandas as pd
from datetime import date, time, datetime

df = pd.read_csv("transactions.small.csv")

df['datetime'] = 0

for index,row in df.iterrows():
    df.set_value(index,'datetime',datetime.datetime.combine(datetime.datetime.strptime(row['date'], "%m/%d/%Y").date(), datetime.datetime.strptime(row['time'], '%H:%M:%S').time()))

df = df.drop('date', 1)
df = df.drop('time', 1)

trans = {}
visited = {}
for index,row in df.iterrows():
    visited[row['source']] = False
    if row['source'] not in trans:
        trans[row['source']] = {}
    if row['target'] not in trans[row['source']]:
        trans[row['source']][row['target']] = []
    trans[row['source']][row['target']].append((row['id'],row['datetime'],row['amount'],row['currency']))



def DFS(key,parent,date,amount,source,depth,flag):
    if (flag):
        flag = False
        print (trans[key].keys())
    elif key == source:
        return "LOL " + parent
    if not flag and depth < 4:
        for target in trans[key].keys():
            print(target)
            for transaction in trans[key][target]:
                if transaction[2] > 100 and transaction[1] > date and transaction[2] < amount:
                    return DFS(target,key,transaction[1],transaction[2],source,depth+1,flag)
        
#print(DFS('02bd318d-57a6-4216-a9d4-e51f1f3fe17d',None,datetime.min, 999999, '02bd318d-57a6-4216-a9d4-e51f1f3fe17d',0,True))
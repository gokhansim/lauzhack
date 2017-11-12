import pandas as pd
from datetime import date, datetime
import time
from datetime import datetime

df1 = pd.read_csv("transactions.csv", chunksize=200000)
df=df1.get_chunk()
df['datetime'] = 0
count_error  = 0
for index,row in df.iterrows():
    try:
        df.set_value(index,'datetime',datetime.combine(datetime.strptime(row['date'], "%m/%d/%Y").date(), datetime.strptime(row['time'], '%H:%M:%S').time()))
    except:
        count_error += 1

df = df.drop('date', 1)
df = df.drop('time', 1)

trans = {}
visited = {}
counts = {}
pairS ={}
pairT ={}
for index,row in df.iterrows():
    visited[row['source']] = False
    if row['source'] not in trans:
        trans[row['source']] = {}
    if row['target'] not in trans[row['source']]:
        trans[row['source']][row['target']] = []
    if row['source'] not in pairS.keys():
        pairS[row['source']] = []
    if row['target'] not in pairT.keys():
        pairT[row['target']] = []

    if  row['target'] not in pairS[row['source']]:
        pairS[row['source']].append(row['target'])

    if  row['source'] not in pairT[row['target']]:
        pairT[row['target']].append(row['source'])

    trans[row['source']][row['target']].append((row['id'],row['datetime'],row['amount'],row['currency']))
    visited[row['id']] = False


print("Possible human trafficing frauders:")
for t in pairT.keys():
    if len(pairT[t]) > 6:
        if t in pairS.keys() and len(pairS[t]) == 1:
            print(t)

print('Finished preprocess')
def DFS(key,parent,date,amount,source,flag,depth,parent_amount):

    if (flag):
        flag = False
    elif key == source and parent_amount - amount < parent_amount / 5:
        #print ("LOL " + parent + " " + key + " " + str(depth))
        return True
    if not flag and depth < 8:
        if key in trans.keys():
            for target in list(trans[key].keys()):
                for transaction in trans[key][target]:
                    if transaction[2] > 1000 and transaction[2] < amount:
                        try:
                            if key == source:
                                if(DFS(target,key,transaction[1],transaction[2],source,flag,depth+1,transaction[2])):
                                    return
                            elif amount - transaction[2] < amount / 10 and (transaction[1] - date).days < 3:
                                if(DFS(target,key,transaction[1],transaction[2],source,flag,depth+1,parent_amount)):
                                    return
                        except:
                            global count_error
                            count_error += 1
for key in trans:
    depth = 0
    DFS(key,None,datetime.min, 999999,key,True,depth,0)

#timepattern(trans)
def DFS_decreasing_diff_start_end(key,date,amount,d, t_id):

    if t_id in visited.keys():
        visited[t_id] = True

    # hill climbing
    if d < 10:
        if key in trans.keys():
            for target in list(trans[key].keys()):
                for transaction in trans[key][target]:
                    if visited[transaction[0]] == False and transaction[2] > 10  and (transaction[2] < amount): #and #(transaction[1] - date).days < 100:
                        # print("key: " + str(key) + " depth " + str(d))
                        return DFS_decreasing_diff_start_end(target,transaction[1],transaction[2],d+1, transaction[0])
                    

d = 0
#t = list(trans[key].keys())[0]
#tt = trans[key][t][0]
ind = 0
for v in visited.keys():
    visited[v] = False

print("Possible flow pattern frauds:")
for key in trans:
    depth = 0
    t = list(trans[key].keys())[0]
    tt = trans[key][t][0]
    DFS_decreasing_diff_start_end(key,datetime.min, 999999,d, tt[0])

        #DFS(key,None,datetime.min, 999999,key,True,depth,0)
        #else:
        #break


# DFS_decreasing_diff_start_end(key,datetime.min, 999999,d, tt[0])
print("Possible time pattern frauds:")
for i in trans:
    for k in trans[i]:
       trans[i][k].sort(key=lambda tup: tup[1])


def timepattern(trans):
    for key in trans:
        for target in trans[key]:
            if len(trans[key][target]) >= 5:
                count = 0
                for index in range (len(trans[key][target]) - 1):
                    if ((trans[key][target][index+1][1] - trans[key][target][index][1]).days < 30
                        and trans[key][target][index][2] >= 500):
                        count += 1
                if (count + 2) > len(trans[key][target]):
                    count = count + 0
                    # print(key, target)
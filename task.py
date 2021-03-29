#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:46:33 2021

@author: niyajaison
"""
# Import your Libraries
# Import your Libraries
import pandas as pd
import csv
import apriori
from apriori import (
   getItemSetTransactionList,
     dataFromFile,
     joinSet,
     printResults,
     returnItemsWithMinSupport,
     runApriori,
     subsets,
 )
title_new=['date','transaction','item']   #naming the titles
data = pd.read_csv('dataset_group.csv',header=None,names=title_new) 

print(data)
data_new=data.drop(['date'],axis=1) #deleting the date column
print(data_new.values[0][1])
transaction_keys=data_new.groupby(['transaction']).groups.keys()

updated_data =[[]]
longest_col=0
print("Upadting dataset to transaction data....")

#making Each transaction at one line with a variable length
for val in range(len(data_new)):
    if(len(updated_data)<((data_new.values[val][0]))):
        updated_data.append([])
    updated_data[(data_new.values[val][0])-1].append(data_new.values[val][1])
#storing the column length to retrive csv data for different column numbers
    if(len(updated_data[(data_new.values[val][0])-1])>longest_col):
        longest_col=len(updated_data[(data_new.values[val][0])-1])
data_file=open('dataset.csv', mode='w',newline='')
#print(updated_data)
#writing the preprocessed csv file
for x in updated_data:
     #print(x)
     data_writer = csv.writer(data_file,delimiter=',')     
     data_writer.writerow(x)
data_file.close()
print("Updated the dataset")
#print("Longest Column = ", longest_col)

# # # Solution # # #
#reading the preprocessed csv file for varying column number
data=pd.read_csv('dataset.csv',header=None,names= list(range(longest_col)))


updated_data =[[]]
k=0 #to discard NAN
for x in data.values:
    updated_data.append([])
    for y in x:
        if(str(y) != "nan"):
            updated_data[k].append(y)
    k=k+1
data.head(7)

items, rules = runApriori(updated_data, 0.15, 0.8)
print ('Case 1 Output:')
printResults(items,rules)


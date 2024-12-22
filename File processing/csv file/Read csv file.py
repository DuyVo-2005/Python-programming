#read with pandas
#import pandas as pd
#df = pd.read_csv("TransferData.csv", sep=",")
#print(df)# print all
#print(df["Time"])# print one column

#read with csv library
import csv
with open('TransferData.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row[0],"\t",row[1])# print two first columns

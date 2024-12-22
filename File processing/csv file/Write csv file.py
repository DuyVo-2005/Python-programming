import pandas as pd
df = pd.read_csv("TransferData.csv", sep=",")
df["Amount_type_str"] = df["Amount"].astype(str)
df.to_csv("TransferData.csv")
#print(df.dtypes)
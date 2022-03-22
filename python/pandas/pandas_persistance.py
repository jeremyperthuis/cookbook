import pandas as pd

# Initialize dataframe from list of dictionaries
df1 = pd.DataFrame([
        {"a":1, "b":2.5, "c":"test1", "d":True},
        {"a":1, "b":2.5, "c":"test2", "d":False},
        {"a":1, "b":2.5, "c":"test3", "d":None}])

# Initialize dataframe from json file
with open("pandas/files/df1.json", "w") as f:
    f.write(df1.to_json(orient="records"))


# Append dictionary to DataFrame
df = df.append({"a":1, "b":2.5, "c":"test1", "d":True}, ignore_index=True)


df2 = pd.read_json("pandas/files/df1.json")
print(df1)
print(pd.normalize(df2)

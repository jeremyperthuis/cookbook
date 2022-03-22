import pandas as pd


df1 = pd.DataFrame([
        {"a":1, "b":2.5, "c":3},
        {"a":4, "b":5.0, "c":6},
        {"a":7, "b":8.76, "c":9}])


# Get first row value of a given column
df1['a'].iloc[0] # returns 1

# Update value in specific column
df1.loc[df1["a"] == 1, 'b'] = 5.6

# Filter dataframe and returns sub DataFrame
df1_1 = df1[(df1["a"] > 1) & ((df1["c"] < 9)| (df1["c"] == 9))]

# Get first 2 rows
df1 = df1.head(2)

# Test if value exist in specific column
4 in df1["a"].to_list() # return True

# Get specific columns value on specific row based on condition
df1["a"].loc[df1["b"]==5].values[0]

# Join str and non str column in another column
df1["d"] = df1[["a", "b"]].astype(str).agg(",".join, axis=1)

# Print all value in c column
print(f":: {', '.join(f'{e}' for e in df1.c)}.")
print(f":: {', '.join(df1['c'].astype(str).to_list())}.")

# replace value with map function
df1["d"] = (
    df1.a.map(
        {
            1:"un",
            2: "deux",
            3: "trois",
            4: "quatre",
            5 : "cinq"
        }
    )
    .fillna("zero")
    .astype(str)
)

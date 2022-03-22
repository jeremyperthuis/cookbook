import pandas as pd


# Concat multiple columns together
df["title"] = df[["title", "comment"]].agg(
            " - ".join, axis=1
        )
print(df)



# display all records
pd.set_option('display.max_rows', None)
# Display all content in each column
pd.set_option('display.max_colwidth', None)
# reinitialize index
df.reset_index(drop=True)



# merging options
df_inner = df.merge(df2, how="inner", on="seatnumber")
df_outer = df.merge(df2, how="outer", on="seatnumber")
df_left = df.merge(df2, how="left", on="seatnumber")
df_right = df.merge(df2, how="right", on="seatnumber")
print("============df_inner=============")
print(df_inner)
print("============df_outer=============")
print(df_outer)
print("============df_left=============")
print(df_left)
print("============df_right=============")
print(df_right)

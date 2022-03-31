import pandas as pd


# Concat multiple columns together
df["title"] = df[["title", "comment"]].agg(
            " - ".join, axis=1)

# Sorting


# display all records
pd.set_option('display.max_rows', None)
# Display all content in each column
pd.set_option('display.max_colwidth', None)
# reinitialize index
df.reset_index(drop=True)

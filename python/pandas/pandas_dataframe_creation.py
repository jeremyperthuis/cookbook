import pandas as pd

# Initialize Dataframe with a dictionnary
d1 = [
    {"a":1, "b":2, "c":3},
    {"a":4, "b":5, "c":6},
    {"a":7, "b":8, "c":9}]

df1 = pd.DataFrame(d1)

# Initialize Dataframe with nested dictionnary
d2 = {'a' : 1, 'b': {'c':2}, 'd':{'e':{'f':3}}}
df2 = pd.json_normalize(d2)


# Initialize Dataframe with specified column types
df3 = pd.DataFrame(
    [[29, "Main title", True, 12.67],
     [30, "Main title2", True, 12.67],
     [14, "Main title3", False, 76.67],
     [7, "Main title4", False, 5.67]],
    columns={'seatnumber': pd.Series(dtype='int'),
            'title': pd.Series(dtype='str'),
            'isvalid': pd.Series(dtype='bool'),
            'price': pd.Series(dtype='float')})



# Add columns with value
d1 = d1.assign(column_new_1=np.nan, column_new_2='dogs', column_new_3=3)

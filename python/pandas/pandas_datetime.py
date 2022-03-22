import pandas as pd
from datetime import datetime, timedelta

df1 = pd.DataFrame([
        {"a":1, "date":"2022-01-01"},
        {"a":4, "date":"2010-01-01"},
        {"a":7, "date":"01/05/2023"}])

# Convert column to datetime
df1['date']= pd.to_datetime(df1['date'])


# Filter by datetime
df1[df1["date"] < datetime.today()] # date before today

df1[df1["date"] < datetime.today() + timedelta(days=120)] # date before today + 120 days

df1[df1["date"] < datetime.strptime("2022-03-01", '%Y-%m-%d')] # date before specific date


# Overlap Detection
# How to test : Decomment meeting_to_insert variable. If existing_meeting dataframe, is empty :
#                   No overlap, if not, it contain all meeting that overlap the new one


df2 = pd.DataFrame([
        {"meeting":"1", "date_debut":"2022-01-04", "date_fin": "2022-01-06"},
        {"meeting":"2", "date_debut":"2022-01-06", "date_fin": "2022-01-10"},
        {"meeting":"3", "date_debut":"2022-01-12", "date_fin": "2022-01-19"},])


# M1 : meeting to insert
# M2 : existing meeting

# Test Overlap 1 : conflit with meeting 1
#   [   M1   ]
#          [   M2   ]
# meeting_to_insert = {"meeting":"4", "date_debut":"2021-01-02", "date_fin": "2022-01-05"}

# Test Overlap 2 : conflit with meeting 3
#           [   M1   ]
#   [   M2   ]
# meeting_to_insert = {"meeting":"4", "date_debut":"2022-01-18", "date_fin": "2022-01-22"}

# Test Overlap 3 : conflit with meeting 2
#   [   M1   ]
#   [   M2   ]
# meeting_to_insert = {"meeting":"4", "date_debut":"2022-01-06", "date_fin": "2022-01-10"}

# Test Overlap 4 : conflit with meeting 3
#  [    M1     ]
#   [   M2   ]
#meeting_to_insert = {"meeting":"4", "date_debut":"2022-01-11", "date_fin": "2022-01-20"}

# Test Overlap 5 : no conflict
#   [   M1   ]
#            [   M2   ]
#meeting_to_insert = {"meeting":"4", "date_debut":"2022-01-02", "date_fin": "2022-01-04"}

# Test Overlap 6 : no conflict
#             [   M1   ]
#   [   M2   ]
#meeting_to_insert = {"meeting":"4", "date_debut":"2022-01-10", "date_fin": "2022-01-12"}


existing_meeting = df2[
    (
        (df2["date_debut"] < meeting_to_insert["date_fin"])
        & (df2["date_fin"] > meeting_to_insert["date_fin"])
    )
    | (
        (df2["date_debut"] < meeting_to_insert["date_debut"])
        & (df2["date_fin"] > meeting_to_insert["date_debut"])
    )
    | (
        (df2["date_debut"] >= meeting_to_insert["date_debut"])
        & (df2["date_fin"] <= meeting_to_insert["date_fin"])
    )

]
print(existing_meeting)

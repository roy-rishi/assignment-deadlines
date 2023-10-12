import pandas

DATA_PATH = "data/2022-24.json"

df = pandas.read_json(DATA_PATH)
print(df)

# pre-process df
for i in range(len(df)):
    # if missing a date, set to null
    if df.at[i, "due"] == "missing value":
        df.at[i, "due"] = pandas.NaT
    if df.at[i, "sub"] == "missing value":
        df.at[i, "sub"] = pandas.NaT
    # isolate name
    if " | Schoology" in df.at[i, "name"]:
        df.at[i, "name"] = df.at[i, "name"].replace(" | Schoology", "")

# convert date strings to datetime objects
df["due"] = pandas.to_datetime(df["due"], format="Due: %A, %B %d, %Y at %I:%M %p")
df["sub"] = pandas.to_datetime(df["sub"], format="%b %d, %Y at %I:%M %p")

# add time delta column (hours early)
timeDeltas = []
for i in range(len(df)):
    # delta in hours
    dayDue = df.at[i, "due"]
    daySub = df.at[i, "sub"]
    # compute delta in hours
    if not pandas.isnull(dayDue) and not pandas.isnull(daySub):
        timeDeltas.append(int((daySub - dayDue).total_seconds() / 3600))
    else:
        timeDeltas.append(pandas.NA)
df["delta (h)"] = timeDeltas

print(df)
df.sort_values(by=["due"], inplace=True)
df.to_csv("data/data_due-sub-name-delta.csv")
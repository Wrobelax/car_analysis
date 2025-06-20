"""This is a script for data cleaning and basic exploration.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import numpy as np
import pandas as pd


# Importing file with cleaned data into dataframe.
source = "../data/auto.csv"
df = pd.read_csv(source, header = None)



"""Checking basic data structure"""
print(df.head()) # Missing data present
print(df.columns) # No headers
print(df.dtypes) # Object, Float and Int
print(df.info)
print(df.describe())
print(df['num-of-doors'].value_counts().idxmax()) # 4 doors is most common type.


# checking missing data.
missing_data = df.isnull()

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")



"""Data cleaning"""
# Setting up headers.
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
         "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
         "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
         "peak-rpm", "city-mpg", "highway-mpg", "price"]

df.columns = headers


# Replacing missing data for all cells.
df = df.replace("?", np.nan)


# Dropping missing data for price.
df = df.dropna(subset = ["price"], axis = 0)


# Replacing NaN with mean value for "normalized-losses" value.
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis = 0)
df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg_norm_loss)


# Replacing NaN with mean value for "bore" value.
avg_bore = df["bore"].astype("float").mean(axis = 0)
df["bore"] = df["bore"].replace(np.nan, avg_bore)


# Replacing NaN with mean value for "stroke" value.
avg_stroke = df["stroke"].astype("float").mean(axis = 0)
df["stroke"] = df["stroke"].replace(np.nan, avg_stroke)


# Replacing NaN with mean value for "horsepower" value.
avg_horsepower = df["horsepower"].astype("float").mean(axis = 0)
df["horsepower"] = df["horsepower"].replace(np.nan, avg_horsepower)


# Replacing NaN with mean value for "peak-rpm".
avg_peak_rpm = df["peak-rpm"].astype("float").mean(axis = 0)
df["peak-rpm"] = df["peak-rpm"].replace(np.nan, avg_peak_rpm)


# Replacing missing values in "num-of-doors" for most common type.
df["num-of-doors"] = df["num-of-doors"].replace(np.nan, "four")


# Correcting data types.
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")



"""Data standardisation and normalization"""
# Converting mpg to L/100km (235 divided by mpg).
df["city-L/100km"] = 235 / df["city-mpg"]
df["highway-mpg"] = 235 / df["highway-mpg"]

df.rename(columns = {"highway-mpg" : "highway-L/100km"}, inplace = True)


# Transforming length, width and height into similar range.
df["length"] = df["length"] / df["length"].max()
df["width"] = df["width"] / df["width"].max()
df["height"] = df["height"] / df["height"].max()


# Resetting index.
df.reset_index(drop = True, inplace = True)


"""Saving corrected file"""
# df.to_csv("../data/auto_cleaned.csv", index = False) # Uncomment to generate file.
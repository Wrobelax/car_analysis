"""This is a script for data analysis, visualisation and outputs generation.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import numpy as np
import pandas as pd
import matplotlib as plt
from matplotlib import pyplot


# Importing file with cleaned data into dataframe.
source = "../data/auto_cleaned.csv"
df = pd.read_csv(source)



"""Data analysis and visualisation"""
# Binning horsepower and creating visualisation.
df["horsepower"] = df["horsepower"].astype(int)
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ["Low", "Medium", "High"]

df["horsepower-binned"] = pd.cut(df["horsepower"], bins, labels = group_names, include_lowest = True)
# df[["horsepower", "horsepower-binned"]].head(20)
# df["horsepower-binned"].value_counts()

plt.pyplot.hist(df["horsepower"], bins = 3, color = "darkred")
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

# pyplot.savefig("../outputs/horsepower_grouping.png") # Saving plot to file.


# Checking for correlations between bore, stroke, compression-ratio and horsepower.
print(df[["bore", "stroke", "compression-ratio", "horsepower"]].corr())
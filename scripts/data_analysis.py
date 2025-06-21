"""This is a script for data analysis, visualisation and outputs generation.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Importing file with cleaned data into dataframe.
source = "../data/auto_cleaned.csv"
df = pd.read_csv(source)



"""Creating variables"""
# Grouping and pivoting body style, drive wheels and price.
df_bdp = df[["drive-wheels", "body-style", "price"]]
grouped_bdp = df_bdp.groupby(["drive-wheels", "body-style"], as_index = False).mean()
grouped_pivot = grouped_bdp.pivot(index = "drive-wheels", columns = "body-style")
grouped_pivot = grouped_pivot.fillna(0)



"""Data analysis and visualisation"""
# Binning horsepower and creating visualisation.
df["horsepower"] = df["horsepower"].astype(int)
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ["Low", "Medium", "High"]

df["horsepower-binned"] = pd.cut(df["horsepower"], bins, labels = group_names, include_lowest = True)
# df[["horsepower", "horsepower-binned"]].head(20)
# df["horsepower-binned"].value_counts()

plt.hist(df["horsepower"], bins = 3, color = "darkred")
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

# pyplot.savefig("../outputs/horsepower_grouping.png") # Saving plot to file.


# Checking for correlations between bore, stroke, compression-ratio and horsepower.
# print(df[["bore", "stroke", "compression-ratio", "horsepower", "engine-size", "price", "body-style"]].corr())


# Visualising relation between engine size and price.
sns.regplot(x = "engine-size", y = "price", data = df)
plt.ylim(0,)
plt.title("Linear regression for engine size and price")
plt.xlabel("Engine size")
plt.ylabel("Price")

# plt.savefig("../outputs/regplot_engsize_price.png") # Saving plot to file.
plt.clf()


# Visualising relation between peak-rpm and price.
sns.regplot(x = "peak-rpm", y = "price", data = df, color = "darkred")
plt.ylim(0,)
plt.title("Linear regression for peak rpm and price")
plt.xlabel("Peak RPM")
plt.ylabel("Price")

# plt.savefig("../outputs/regplot_peakrpm_price.png") # Saving plot to file.
plt.clf()


# Visualising relation between peak-rpm and price.
sns.regplot(x = "stroke", y = "price", data = df, color = "darkgreen")
plt.ylim(0,)
plt.title("Linear regression for stroke and price")
plt.xlabel("Stroke")
plt.ylabel("Price")

# plt.savefig("../outputs/regplot_stroke_price.png") # Saving plot to file.
plt.clf()


# Visualising relation between body-style and price.
sns.boxplot(x = "body-style", y = "price", data = df, color = "violet")
plt.ylim(0,)
plt.title("Correlation between body style and price")
plt.xlabel("Body style")
plt.ylabel("Price")

# plt.savefig("../outputs/boxplot_bstyle_price.png") # Saving plot to file.
plt.clf()


# Visualising relation between body-style and price.
sns.boxplot(x = "drive-wheels", y = "price", data = df, color = "skyblue")
plt.ylim(0,)
plt.title("Correlation between drive wheels and price")
plt.xlabel("Drive wheels")
plt.ylabel("Price")

# plt.savefig("../outputs/boxplot_dwheels_price.png") # Saving plot to file.
plt.clf()


# Visualising correlation between price and driving wheels vs. body style.
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap ="RdBu")

row_labels = grouped_pivot.columns.levels[1]
col_labels =grouped_pivot.index

ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor = False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor = False)

ax.set_xticklabels(row_labels, minor = False)
ax.set_yticklabels(col_labels, minor = False)

plt.xticks(rotation = 90)
fig.colorbar(im)
# plt.savefig("../outputs/heatmap_corr_price.png") # Saving plot to file.
plt.clf()
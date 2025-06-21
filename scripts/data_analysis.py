"""This is a script for data analysis, visualisation and outputs generation.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


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


# Linear regression for highway-L/100km and price.
lm = LinearRegression()
X = df[["highway-L/100km"]]
Y = df["price"]
lm.fit(X,Y)
y_predict = lm.predict(X)

sns.regplot(x = X, y = Y)
plt.title("Linear regression for liter per 100km and price")
plt.xlabel("L/100km")
plt.ylabel("Price")

# plt.savefig("../outputs/regplot_highway_price.png") # Saving plot to file.
plt.clf()


# Residual plot for highway-L/100km and price.
plt.figure(figsize = (12, 10))
sns.residplot(x = X, y = Y, color = 'darkred')
plt.title("liter per 100km and price")
plt.xlabel("L/100km")
plt.ylabel("Price")

# plt.savefig("../outputs/resid_highway_price.png") # Saving plot to file.
plt.clf()


# Visualising multiple linear regression for horsepower, curb-weight, engine-size, highway-L/100km and price.
X1 = df[["horsepower", "curb-weight", "engine-size", "highway-L/100km"]]
Y1 = df["price"]
lm1 = LinearRegression()
lm1.fit(X1, Y1)
y_hat = lm1.predict(X1)

plt.figure(figsize = (12,10))
ax1 = sns.distplot(df["price"], hist = False, color = "r", label = "Actual value")
sns.distplot(y_hat, hist = False, color = "b", label = "Fitted values", ax = ax1)
plt.title("Actual vs fitted values for price")
plt.xlabel("Price")
plt.ylabel("Proportion of cars")

# plt.savefig("../outputs/multi_lin_reg.png") # Saving plot to file.
plt.clf()


# Visualising polynomial regression.
X2 = df["highway-L/100km"]
Y2 = df["price"]
f = np.polyfit(X2, Y2, 3)
p = np.poly1d(f)

x_new = np.linspace(X2.min(), X2.max(), 100)
y_new = p(x_new)

plt.plot(X2, Y2, '.', x_new, y_new, '-')
plt.title("Polynomial Fit with Matplotlib for Price ~ Gasoline consumption")
ax = plt.gca()
ax.set_facecolor((0.898, 0.898, 0.898))
fig = plt.gcf()
plt.xlabel("Gasoline consumption in litres/100km")
plt.ylabel('Price of Cars')

# plt.savefig("../outputs/poly_reg.png") # Saving plot to file.
plt.clf()


# Visualising polynomial regression of 11th degree (overfitting).
X2 = df["highway-L/100km"]
Y2 = df["price"]
f = np.polyfit(X2, Y2, 11)
p = np.poly1d(f)

x_new = np.linspace(X2.min(), X2.max(), 100)
y_new = p(x_new)

plt.plot(X2, Y2, '.', x_new, y_new, '-')
plt.title("Polynomial Fit with Matplotlib for Price ~ Gasoline consumption")
ax = plt.gca()
ax.set_facecolor((0.898, 0.898, 0.898))
fig = plt.gcf()
plt.xlabel("Gasoline consumption in litres/100km")
plt.ylabel('Price of Cars')

# plt.savefig("../outputs/poly_overfitted_reg.png") # Saving plot to file.
plt.clf()



"""Training and testing"""
# Price.
y_data = df["price"]
x_data = df.drop("price", axis = 1)

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.2, random_state = 1)


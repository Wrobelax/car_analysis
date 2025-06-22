**Project status**: Completed - closed.

This project is a data analysis of a publicly available data from: 
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv

The project consists of data analysis, data modeling training and testing of used car prices by using Pandas, Matplotlib, Seaborn, Scikit Learn and Numpy Python libraries. 
All data was pushed and managed on Github via Git bash. The data did not require cleaning so this step was omitted.


**Structure of the project is as follows:**


_Folder "data":_
- "auto.csv" : File with input data used for cleaning.
- "auto_cleaned.csv" : Cleaned data used for data analysis and visualisation.


_Folder "scripts":_
- "data_cleaning.py" : Python file used for data cleaning, basic exploration of data and generating 'auto_cleaned.csv'.
- "data_analysis.py" : Python file used for data analysis and visualisation. Used 'auto_cleaned.csv'.


_Folder "outputs":_
- "boxplot_bstyle_price.png" : Box plot describing correlation between body style and price.
- "boxplot_dwheels_price.png" : Box plot describing correlation between drive wheels and price.
- "heatmap_corr_price.png" : Heatmap describing correlation between car type and driving wheels vs. price.
- "horsepower_grouping.png" : Bar chart describing number of cars and horsepower.
- "multi_lin_reg.png" : Multiple linear regression describing actual vs. fitted value for price.
- "multiple_reg_train.png" : Multiple linear regression describing distribution of predicted value using training and test data.
- "poly_overfitted_reg.png" : Polynomial regression plot describing overfitted regression gasoline consumption and car price.
- "poly_reg.png" : Polynomial regression plot describing properly fitted regression gasoline consumption and car price.
- "regplot_engsize_price.png" : Regression plot for engine size and price.
- "regplot_highway_price.png" : Regression plot for gasoline consumption in litres per 100 km vs. price.
- "regplot_peakrpm_price.png" : Regression plot for peak RPM of an engine size and price.
- "regplot_stroke_price.png" : Regression plot for stroke and car price.
- "resid_highway_price.png" : Residual plot for gasoline consumption per liter on 100km and price.
- "ridge_reg.png" : Ridge regression plot for trained and tested data.
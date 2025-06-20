"""This is a script for data exploration and visualisation used for generating outputs.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import numpy as np
import pandas as pd
from pyodide.http import pyfetch

# Importing file with cleaned data into dataframe.
source = "../data/Historical_Wildfires.csv"
df = pd.read_csv(source)
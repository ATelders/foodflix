# Import modules
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
print("Setup Complete")

# Load the data from the csv file in a dataframe
file_path = "data/02_intermediate/intermediate.csv"
df = pd.read_csv(file_path)

# Takes a sample of 10000 rows from the dataframe
df_sample = df.sample(n=10000, random_state=1)
profile = ProfileReport(df_sample, title='Pandas Profiling Report')

# Saves the report to a html page
profile.to_file("results/profiling_intermediate.html")
# Import modules
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
print("Setup Complete")

# Load the data from the tsv file in a dataframe
file_path = "/home/apprenant/simplon_projects/foodflix/data/01_raw/en.openfoodfacts.org.products.tsv"
df = pd.read_csv(file_path, sep='\t')

# Takes a sample of 10000 rows from the dataframe
df_sample = df.sample(n=10000, random_state=1)
profile = ProfileReport(df_sample, title='Pandas Profiling Report')

# Saves the report to a html page
profile.to_file("results/profiling_raw.html")
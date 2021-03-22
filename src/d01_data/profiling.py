import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
print("Setup Complete")

file_path = "/home/apprenant/simplon_projects/foodflix/data/01_raw/en.openfoodfacts.org.products.tsv"
df = pd.read_csv(file_path, sep='\t')

df_sample = df.sample(n=10000, random_state=1)
profile = ProfileReport(df_sample, title='Pandas Profiling Report')

profile.to_file("your_report.html")
# This code summarizes the cleaning code that is in the notebook 2021-03-21-at-data-cleaning.ipynb

import pandas as pd

print("Setup Complete")

# After dowloading tsv file, I read it with pandas
df = pd.read_csv(r"/home/apprenant/simplon_projects/foodflix/data/01_raw/en.openfoodfacts.org.products.tsv", sep='\t')

# This Series 
percent_of_nans = df.isnull().sum() / df.shape[0] * 100

useless_features = percent_of_nans[percent_of_nans > 98].index

clean_df = df.drop(columns=useless_features)

clean_df = clean_df[
['product_name',
 'brands',
 'ingredients_text',
 'nutrition_grade_fr',
 'energy_100g',
 'fat_100g',
 'saturated-fat_100g',
 'carbohydrates_100g',
 'sugars_100g',
 'fiber_100g',
 'proteins_100g',
 'salt_100g']
]

clean_df = clean_df.dropna(subset= [
 'energy_100g',
 'fat_100g',
 'saturated-fat_100g',
 'carbohydrates_100g',
 'sugars_100g',
 'fiber_100g',
 'proteins_100g',
 'salt_100g'],how ='all')


energy_outliers = clean_df.loc[clean_df['energy_100g'] > 3800]
clean_df.drop(energy_outliers.index, axis=0, inplace=True)

clean_df.to_csv('data/02_intermediate/intermediate.csv')
#!/usr/bin/env python
# coding: utf-8

import lux
import pandas as pd

print("Setup Complete")

file_path = "/home/apprenant/simplon_projects/foodflix/data/01_raw/en.openfoodfacts.org.products.tsv"
df = pd.read_csv(file_path, sep='\t')

percent_of_nans = df.isnull().sum().sort_values(ascending=False) / df.shape[0] * 100

useless_features = percent_of_nans[percent_of_nans > 99].index
useless_features

clean_df = df.drop(columns=useless_features)

clean_df['fruits-vegetables-nuts_100g'] = df['fruits-vegetables-nuts_100g']

columns = list(clean_df.columns)
columns

clean_df["countries"].str.replace(r".*(fr).*", "France", case=False, regex=True)

clean_df = clean_df.loc[clean_df['countries'] == 'France']

clean_df = clean_df[
['product_name',
 'brands',
 'countries',
 'ingredients_text',
 'nutrition_grade_fr',
 'energy_100g',
 'fat_100g',
 'saturated-fat_100g',
 'carbohydrates_100g',
 'sugars_100g',
 'fiber_100g',
 'proteins_100g',
 'salt_100g',
 'nutrition-score-fr_100g',
 'fruits-vegetables-nuts_100g'
 ]
]

clean_df.save_as_html('/home/apprenant/simplon_projects/foodflix/results/lux_report_1.html')


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
clean_df = clean_df.drop(energy_outliers.index, axis=0)

clean_df.loc[clean_df['energy_100g'] < (clean_df['fat_100g'] * 37) + ((clean_df['carbohydrates_100g'] + clean_df['proteins_100g']) * 17)]

list_to_clean = ['fat_100g',
 'saturated-fat_100g',
 'carbohydrates_100g',
 'sugars_100g',
 'fiber_100g',
 'proteins_100g',
 'salt_100g']

outliers_df = pd.DataFrame()

for item in list_to_clean:
    outliers_more = clean_df.loc[clean_df[item] > 100]
    outliers_less = clean_df.loc[clean_df[item] < 0]
    clean_df = clean_df.drop(outliers_more.index, axis=0)
    clean_df = clean_df.drop(outliers_less.index, axis=0)   

clean_df['calculated_energy'] = (clean_df['fat_100g'] * 38) + ((clean_df['carbohydrates_100g'] + clean_df['proteins_100g']) * 17)


clean_df.to_csv('/home/apprenant/simplon_projects/foodflix/data/02_intermediate/intermediate.csv')
print("Saved data to intermediate.csv")
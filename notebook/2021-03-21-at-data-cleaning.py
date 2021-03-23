#!/usr/bin/env python
# coding: utf-8

# Import the needed libraries for data visualisation

# In[1]:


import lux
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import missingno as msno
import re
print("Setup Complete")


# Import the data from the tsv file with pandas

# In[2]:


file_path = "/home/apprenant/simplon_projects/foodflix/data/01_raw/en.openfoodfacts.org.products.tsv"
df = pd.read_csv(file_path, sep='\t')


# Looking at the shape of the data : how many lines and how many columns

# In[3]:


df.shape


# In[4]:


percent_of_nans = df.isnull().sum().sort_values(ascending=False) / df.shape[0] * 100


# In[5]:


useless_features = percent_of_nans[percent_of_nans > 98].index
useless_features


# In[6]:


clean_df = df.drop(columns=useless_features)
#clean_df


# In[7]:


#msno.matrix(clean_df)


# In[8]:


#list(clean_df.columns)


# In[9]:


clean_df.shape


# In[10]:


clean_df["countries"] = clean_df["countries"].apply(
    lambda x: "France" if re.match(r".*(fr).*", str(x), re.IGNORECASE) else x
)


# In[12]:


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
 'nutrition-score-fr_100g']
]


# In[14]:


clean_df = clean_df.loc[clean_df['countries'] == 'France']


# In[15]:


clean_df


# In[16]:


clean_df.save_as_html('/home/apprenant/simplon_projects/foodflix/results/1st.html')


# In[17]:


clean_df.shape


# In[18]:


clean_df = clean_df.dropna(subset= [
 'energy_100g',
 'fat_100g',
 'saturated-fat_100g',
 'carbohydrates_100g',
 'sugars_100g',
 'fiber_100g',
 'proteins_100g',
 'salt_100g'],how ='all')


# In[19]:


clean_df.shape


# In[20]:


clean_df


# In[26]:


energy_outliers = clean_df.loc[clean_df['energy_100g'] > 3800]
clean_df = clean_df.drop(energy_outliers.index, axis=0)


# Visualise rows where energy > 3800
# Visualise rows where fat <

# In[40]:


clean_df.shape


# In[42]:


clean_df.loc[clean_df['energy_100g']]


# In[41]:


clean_df.loc[clean_df['energy_100g'] < (clean_df['fat_100g'] * 37) + ((clean_df['carbohydrates_100g'] + clean_df['proteins_100g']) * 17)]


# In[28]:


clean_df


# In[51]:


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

clean_df



# In[53]:


clean_df.shape


# In[63]:


clean_df['calculated_energy'] = (clean_df['fat_100g'] * 38) + ((clean_df['carbohydrates_100g'] + clean_df['proteins_100g']) * 17)



#clean_df.loc[clean_df['energy_100g'] < (clean_df['fat_100g'] * 38) + ((clean_df['carbohydrates_100g'] + clean_df['proteins_100g']) * 17)]


# In[56]:


clean_df


# In[64]:


clean_df['energy_100g'].corr(clean_df['calculated_energy'])


# In[65]:


clean_df['energy_100g'].plot()


# In[66]:


clean_df['calculated_energy'].plot()


# In[70]:


msno.matrix(clean_df)


# In[79]:



empty_score = clean_df.loc[clean_df['nutrition-score-fr_100g'].isna()]
empty_score


# Import modules
import pandas as pd
import sys
sys.path.insert(0, "/home/apprenant/simplon_projects/foodflix/")
from src.d00_utils.mysql_utils import mysql_connect, save_to_mysql
from conf.conf import mysql_pseudo, mysql_mdp

# After dowloading my xlsx and csv files, I read them with pandas
df = pd.read_csv(r"/home/apprenant/simplon_projects/foodflix/data/01_raw/en.openfoodfacts.org.products.tsv", sep='\t')

#Create connection with mysql
connect = mysql_connect()

# Save the table in mysql database

save_to_mysql(db_connect=connect,df_to_save=df,df_name='food_data')
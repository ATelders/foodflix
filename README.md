# foodflix

The original data is in the 'data/01_raw' folder

Once cleaned, it goes into the 'data/02_intermediate' folder

In the notebook folder, there are two files to check :
'2021-03-20-at-raw-data-analysis.ipynb'
'2021-03-21-at-data-cleaning.ipynb'

In the results folder, the 'profiling_raw.html' and 'profiling_intermediate.html' are for data visualisation.
Both were created over a sample of 10000 rows.

In the 'src/d00_utils' folder, there is one file 'mysql_utils.py'
    This file defines the functions to connect and to save to MySQL. Eventually I chose to leave these functions there, but 
    not to use them because I couldn't load the original data because of its size. This has something to do with the InnoDB engine.

In the 'src/d01_data' folder, there is the 'load_data.py', which is not used for the reason explained just above.
The 'clean_data.py' runs the same commands that the cleaning notebook, and saves the results in 'data/02_intermediate/intermediate.csv'
The 'profiling.py' creates a html report with the raw data and saves it in 'results'

In the 'src/d02_intermediate' folder, the 'profiling.py' creates a html report with the cleaned data and saves it in 'results'.

The 'requirements.txt' lists the libraries installed in the Python3 enviromnment, it was created using 'pip freeze > requirements.txt'
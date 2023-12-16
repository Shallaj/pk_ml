import os
import subprocess
import numpy as np
import pandas as pd


# This snippet assumes you run setup first

# This code copies file in your Google Bucket and loads it into a dataframe

# Replace 'test.csv' with THE NAME of the file you're going to download from the bucket (don't delete the quotation marks)
name_of_file_in_bucket = 'index_date.csv'

########################################################################
##
################# DON'T CHANGE FROM HERE ###############################
##
########################################################################

# get the bucket name
my_bucket = os.getenv('WORKSPACE_BUCKET')

# copy csv file from the bucket to the current working space
os.system(f"gsutil cp '{my_bucket}/data/{name_of_file_in_bucket}' .")

print(f'[INFO] {name_of_file_in_bucket} is successfully downloaded into your working space')
# save dataframe in a csv file in the same workspace as the notebook
my_dataframe = pd.read_csv(name_of_file_in_bucket)
my_dataframe.head()

import pandas as pd

def drug_parser(drug_df, my_dataframe, drug_name):
    merged_df = pd.merge(drug_df, my_dataframe, on='person_id', how='left')
    merged_df['index_date'] = pd.to_datetime(merged_df['index_date'], format='%m %d %Y').dt.tz_localize(None)
    merged_df['drug_exposure_start_datetime'] = pd.to_datetime(merged_df['drug_exposure_start_datetime'], format='%m %d %Y').dt.tz_localize(None)
    merged_df = merged_df[merged_df['drug_exposure_start_datetime'] < merged_df['index_date']]
    merged_df = merged_df.drop_duplicates(subset='person_id', keep='first')
    
    tidy_drug_name = pd.DataFrame(columns = ['person_id', drug_name])
    tidy_drug_name['person_id'] = merged_df['person_id']
    tidy_drug_name[drug_name] = 1
    print(tidy_drug_name)
    
    return tidy_drug_name  # return the dataframe
drug_df= #enter the df name here
drug_name='' #enter the drug name here
# Call the function and assign the result to a variable
tidy = drug_parser(drug_df, my_dataframe, drug_name)

# Now you can print tidy outside of the function
print(tidy)
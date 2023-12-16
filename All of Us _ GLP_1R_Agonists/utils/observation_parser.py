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
def observation_parser(observation_df, my_dataframe, observation_name):
    merged_df = pd.merge(observation_df, my_dataframe, on='person_id', how='left')
    merged_df['index_date'] = pd.to_datetime(merged_df['index_date'], format='%m %d %Y').dt.tz_localize(None)
    merged_df['observation_datetime'] = pd.to_datetime(merged_df['observation_datetime'], format='%m %d %Y').dt.tz_localize(None)
    merged_df = merged_df[merged_df['observation_datetime'] < merged_df['index_date']]
    merged_df = merged_df.drop_duplicates(subset='person_id', keep='first')
    
    tidy_observation_name = pd.DataFrame(columns = ['person_id', observation_name])
    tidy_observation_name['person_id'] = merged_df['person_id']
    tidy_observation_name[observation_name] = 1
    print(tidy_observation_name)
    
    return tidy_observation_name  # return the dataframe
observation_df=  #enter the df name here
observation_name= '' #enter the observation name here
# Call the function and assign the result to a variable
tidy1 = observation_parser(observation_df, my_dataframe, observation_name)

# Now you can print tidy outside of the function
print(tidy1)
import pandas as pd

def condition_parser(condition_df, my_dataframe, condition_name):
    merged_df = pd.merge(condition_df, my_dataframe, on='person_id', how='left')
    print(merged_df)

    merged_df['final_index_date'] = pd.to_datetime(merged_df['final_index_date'], format='%m %d %Y').dt.tz_localize(None)
    merged_df['condition_start_datetime'] = pd.to_datetime(merged_df['condition_start_datetime'], format='%m %d %Y').dt.tz_localize(None)

    merged_df = merged_df[merged_df['condition_start_datetime'] < merged_df['final_index_date']]
    merged_df = merged_df.drop_duplicates(subset='person_id', keep='first')

    print(merged_df)

    tidy_condition_name = pd.DataFrame(columns = ['person_id', condition_name])
    tidy_condition_name['person_id'] = merged_df['person_id']
    tidy_condition_name[condition_name] = 1
    print(tidy_condition_name)
    
# Assuming condition_df, my_dataframe, and condition_name are defined
condition_df = dataset_40910266_condition_df  # replace with your actual dataframe
condition_name = 'mi'  # replace with your actual condition name

# Call the function
condition_parser(condition_df, my_dataframe, condition_name)
    
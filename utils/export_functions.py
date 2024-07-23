import os

def export_df_to_csv(df, brand):
    '''
    Function to export a pandas DataFrame to a csv-file
    '''

    # create the folder if it does not exist yet
    if not os.path.exists("data"):
        os.mkdir("data")
    
    # compose the folder
    folder_name = f"data/{brand}"
    os.makedirs(folder_name, exist_ok=True)

    # compose the file name
    file_name = f"{folder_name}/{brand}.csv"

    # export the DataFrame to csv
    df.to_csv(file_name)
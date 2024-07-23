import pandas

def convert_list_to_df(objects_list):
    '''
    Function to create a pandas DataFrame from a list of objects
    '''
    # conver the list to a DataFrame
    df = pandas.DataFrame(objects_list)
    
    return df
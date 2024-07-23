from utils.import_functions import import_car
from utils.conversion__functions import convert_list_to_df
from utils.export_functions import export_df_to_csv

# specify the selection
import_type = input("Import cars by brand (brand) or by license plate (plate):\n") or "brand"

# ask for the brand
selected_values = input("Specify values:\n")

# split the sting to a list
selected_values_list = selected_values.split(" ")

# loop through the brands
for selected_value in selected_values_list:
    print(f"Importing {selected_value}")
    # use the brand to import
    try:
        cars_list = import_car(selected_value, import_type)
    except ValueError:
        print(f"No cars found for {selected_value}")
        continue

    # convert the list of cars to a pandas DataFrame
    cars_df = convert_list_to_df(cars_list)

    # export the DataFrame to a csv-file
    export_df_to_csv(cars_df, selected_value)
import requests

def import_car(value, plate_or_brand):
    # uppercase the brand
    value_upper = value.upper()

    # based on selection for plate of brand
    if plate_or_brand == "brand":
        # compose the endpoint
        endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={value_upper}"
    elif plate_or_brand == "plate":
        endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={value_upper}"
    else:
        raise ValueError("plate_or_brand parameter should be 'plate' or 'brand'")

    # send the request to the endpoint
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    # if the data is empty
    if len(data) == 0:
        raise ValueError(f"No cars found for brand: '{value}'")
    
    return data
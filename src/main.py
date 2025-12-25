import json
import os
from transform.transform import extract_iaqi_data
import pandas as pd

def inspect_raw():

    base_dir = os.path.dirname(os.path.dirname(__file__))
    raw_path = os.path.join(base_dir, "data","raw","aqi_raw.json")

    with open(raw_path, "r") as f:
        data = json.load(f)

    #lets pick the first city
    first_city = next(iter(data))
    # print("City Key: ", first_city)
    # print("\n raw json for this city:\n")
    # print(json.dumps(data[first_city],indent = 4))

    city_payload = data[first_city]
    iaqi = city_payload["data"]["iaqi"]

    # print(iaqi, "IAQI for", first_city)
    print(iaqi.keys())
    print(iaqi.values())
    print("PM.5 value", iaqi["pm25"]["v"])
    print("PM2.5 value", iaqi.get("pm25",{}).get("v"))

    record = extract_iaqi_data(first_city, data[first_city])
    print("this is new logic", record)

    records = [] #empty list
    for city_name, city_payload in data.items():
        print("Processing city", city_name)
        record = extract_iaqi_data(city_name, city_payload)
        records.append(record) #adding dictionary into the list

    df_aqi = pd.DataFrame(records) #convert to dataframe

#Adding AQI business logic
    def categorise_aqi(pm25):
        if pd.isna(pm25):
            return "Not available"
        elif pm25 <= 30:
            return "Good Air"
        elif pm25 <= 60:
            return "Satisfactory Air"
        elif pm25 <= 90:
            return "Moderate Air"
        elif pm25 <= 120:
            return "Poor Air"
        elif pm25 <= 250:
            return "Very Poor Air"
        else:
            return "severe"
    df_aqi["Category Air Quality"] = df_aqi["pm25"].apply(categorise_aqi)
    #adding new category column into our data fram applied business logic

    #Load to CSV
    processed_dir = os.path.join(base_dir, "data","processed")
    output_dir = os.path.join(processed_dir, "aqi_clean.csv")

    df_aqi.to_csv(output_dir, index = False) #here we are converting dictionary into csv and loading it.
    print("dataframe written to {output_dir}")

    print(df_aqi.head())
    print(df_aqi.info())

if __name__ == "__main__":
    inspect_raw()


    #next step to convert data into dataframe.
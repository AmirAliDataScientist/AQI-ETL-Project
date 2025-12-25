import requests
import json
import os

from config_loader import load_config

def fetch_city_api(base_url, city, token):
    url = f"{base_url}/{city}/?token={token}" #creating the url

    try:
        response = requests.get(url, timeout = 10)
        response.raise_for_status()
        return response.json()

    except Exception as e:
        print(f"Erorr fethcing data for {city}: {e}")
        return None



def extract_data():
    config = load_config()
    base_url = config['api']['base_url']
    cities = config['api']['cities']
    token = config['api']['token']

    all_city_data ={} #empty dictionary to store all cieties json data

    for city in cities:
        print("Fetching data for :",city)

        data = fetch_city_api(base_url, city, token)

        if data and data.get("status") == "ok":
            print("Ok")
            all_city_data[city] = data
        else:
            print("Failed")
            all_city_data[city] = {"status":"Failed"}

    #save raw data into json file
    base_dir = os.path.dirname(os.path.dirname(__file__))
    raw_path = os.path.join(base_dir,config['paths']['raw_data'])

    #Create dictionary if its not exist
    os.makedirs(os.path.dirname(raw_path),exist_ok = True)
    with open(raw_path,'w') as f:
        json.dump(all_city_data,f, indent = 4)
    print("raw data saved to {raw_path}")

    return all_city_data

if __name__ == "__main__":
    extract_data()


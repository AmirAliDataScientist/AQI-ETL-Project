import os
import yaml

def load_config():

    """
    config/config.yaml and perform basic validation.
    return the configration as python dictionary
    """

    #Step lets get to the start directory using os.path.dirname
    #--file-- is use for to get the current location of the file we are on

    base_dir = os.path.dirname(os.path.dirname(__file__)) #

    #Step 2: Lets go to the config.yaml file which is in start directory - config - config.yaml

    config_file = os.path.join(base_dir,"config","config.yaml")

    #Lets put a validation and check if file exists

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"config file is not found: {config_file}")
    #Step 4 Open and load yaml
    with open(config_file,'r') as f:
        config = yaml.safe_load(f)

    #step 5 basic validation
    return_api_key = ["base_url", "token", "cities" ]
    for key in return_api_key:
        if key not in config.get('api',{}):
            raise KeyError(f"API key is missing {key}")


    required_paths = ['raw_data', 'processed_data']
    for key in required_paths:
        if key not in config.get('paths',{}):
            raise KeyError(f"Missing required path:{key}")

    return config
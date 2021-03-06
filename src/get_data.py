# Get the data source from params.yaml and return a dataframe

import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:       # TO read the config(params.yaml) file
        config = yaml.safe_load(yaml_file)     # Parse YAML document and produce the corresponding Python object
    return config                              # Return the config file

def get_data(config_path):
    config = read_params(config_path)
    #print(config)
    data_path = config["data_source"]["s3_source"]          # To get only the datasource - s3_source
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')  # To read the dataset
    #print(df.head())
    return df                                               # Return dataframe



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)
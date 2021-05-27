# Split the raw data and Save it in data/processed folder

import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_saved_data(config_path):
    config = read_params(config_path)                        # To read the config file
    test_data_path = config["split_data"]["test_path"]       # Test data path from config file
    train_data_path = config["split_data"]["train_path"]     # Train data path from config file
    raw_data_path = config["load_data"]["raw_dataset_csv"]   # Raw data Path from config file
    split_ratio = config["split_data"]["test_size"]          # To split Ratio from config file
    random_state = config["base"]["random_state"]            # Random State from the config file

    df = pd.read_csv(raw_data_path, sep=",")                 # To split the data from the raw_data
    train, test = train_test_split(
        df, 
        test_size=split_ratio, 
        random_state=random_state
        )
    train.to_csv(train_data_path, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)


# Read the data from Data source and Save it in the data/raw for further process

from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)                                 # Load & Read the config file
    df = get_data(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns]          # Replace column without space with new column
    raw_data_path = config["load_data"]["raw_dataset_csv"]            # Read the params.yaml file
    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)   # Save the Data to data/raw/winequality.csv


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)
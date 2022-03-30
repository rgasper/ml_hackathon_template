from eis.EISDataIO import eis_dataframe_from_csv, eis_dataframe_to_csv
import pandas as pd


if __name__ == "__main__":
    train_data = eis_dataframe_from_csv("train_data.csv")
    train_data = train_data.sample(frac=0.1).reset_index(drop=True)
    train_data_split = train_data.sample(frac=0.8).reset_index(drop=True)
    test_data_split = train_data[~train_data.index.isin(train_data_split.index)].reset_index(drop=True)
    eis_dataframe_to_csv(train_data_split, "example_pipeline/stage_data/train_data.csv")
    eis_dataframe_to_csv(test_data_split, "example_pipeline/stage_data/test_data.csv")

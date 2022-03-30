from typing import Any
from eis.EISDataIO import eis_dataframe_from_csv, eis_dataframe_to_csv
import pandas as pd


def random_classify(train_data: pd.DataFrame, test_data: pd.DataFrame) -> pd.DataFrame:
    def get_random_circuit(_: Any):
        return train_data.sample(n=1).iloc[0]["Circuit"]

    circuit_guesses = test_data.copy()
    circuit_guesses["Circuit"] = test_data["freq"].apply(get_random_circuit)
    return circuit_guesses


if __name__ == "__main__":
    train_data = eis_dataframe_from_csv("example_pipeline/stage_data/train_data.csv")
    test_data = eis_dataframe_from_csv("example_pipeline/stage_data/test_data.csv")
    circuit_guesses = random_classify(train_data, test_data)
    eis_dataframe_to_csv(pd.DataFrame(circuit_guesses["Circuit"]), "example_pipeline/stage_data/circuit_guesses.csv")

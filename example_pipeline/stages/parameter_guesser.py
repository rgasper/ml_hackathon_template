from eis.EISDataIO import (
    eis_dataframe_from_csv,
    eis_dataframe_to_csv,
    parse_circuit_params_from_str,
    circuit_params_dict_to_str,
)
import pandas as pd


def all_params_are_one(train_data: pd.DataFrame, circuit_guesses: pd.DataFrame) -> pd.DataFrame:
    params_str_lookup = {}
    for circuit_name in train_data.Circuit.unique():
        sample = train_data.loc[train_data.Circuit == circuit_name].iloc[0]
        params_str_lookup[sample.Circuit] = sample.Parameters

    def get_params(circuit: str) -> str:
        params_str = params_str_lookup[circuit]
        params = parse_circuit_params_from_str(params_str)
        for key in params:
            params[key] = 1
        return circuit_params_dict_to_str(params)

    circuit_guesses["Parameters"] = circuit_guesses["Circuit"].apply(get_params)
    return circuit_guesses


if __name__ == "__main__":
    train_data = eis_dataframe_from_csv("example_pipeline/stage_data/train_data.csv")
    circuit_guesses = eis_dataframe_from_csv("example_pipeline/stage_data/circuit_guesses.csv")
    submission = all_params_are_one(train_data, circuit_guesses)
    eis_dataframe_to_csv(submission, "example_pipeline/stage_data/submission.csv")

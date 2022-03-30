from eis.scoring import ECM_class_classification_scorer, ECM_params_initial_guess_scorer
from eis.EISDataIO import eis_dataframe_from_csv
import json

if __name__ == "__main__":
    test_data = eis_dataframe_from_csv("example_pipeline/stage_data/test_data.csv")
    submission = eis_dataframe_from_csv("example_pipeline/stage_data/submission.csv")

    metrics = {}
    metrics["classification_accuracy"] = ECM_class_classification_scorer(test_data["Circuit"], submission["Circuit"])
    metrics["parameter_guessing_loss"] = ECM_params_initial_guess_scorer(test_data[["freq", "Z"]], submission)
    with open("example_pipeline/stage_data/metrics.json", "w") as f:
        json.dump(metrics, f)

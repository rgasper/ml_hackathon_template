# Repository Readme

This is an example of the template we built for the 2022 BatteryDEV hackathon. It has had the data files redacted for the purpose of being generally shared. It was created with the assistance of fellow members of the BatteryDev 2022 volunteer team: Anoushka Bhutani, Masaki Adachi, and Joachim Schaeffer.

This document is the repository readme - covering the data, some technical submission guidelines, source code, and execution environments that have already been provided to you. For a more general overview of the challenge, see the [Challenge Description](Challenge.md).

## What's the code that's already in here?

To help all contestants get started quickly with solving the interesting problems in the challenge, some code and structure has been prepared already in this repository. In [eis/](eis/), there is python source code for reading & writing the EIS data files, creating ECMs, and scoring model outputs for both challenge tasks. The official scoring functions that will be used on your submissions are also in this library, so you can test your model(s) and directly see improvement in the same metrics the judges will see. If you're planning using another programming language, we've tried to keep the code clean and well documented to help inspire your solutions for EIS data so you can spend more time innovating new & interesting ideas.

There is a single CLI application in the library, used for scoring submissions - [scoring.py](eis/scoring.py). This can be used to score a properly formatted CSV with no python knowledge necessary. run `python scoring.py --help` for details. This module contains many importable functions for the scoring methods if you'd prefer to implement them directly, including a standard ECM RMSE scorer that's not used for the competition scoring.  

Examples of using this code can be found in [notebooks/](notebooks/), and also in the automated tests. The tests may be helpful for understanding the interfaces and behaviors of the functions. In particular, [eis/test_circuit_parsing.py](eis/test_circuit_parsing.py) contains working examples of the flexibility in providing parameters to circuit models, and how to register a new circuit model if you'd like to do so. There are utility functions for reading and writing the EIS data csvs, which we recommend you use to generate model output for your submission in [EISDataIO.py](eis/EISDataIO.py). There are also utility functions for plotting EIS spectra, with and without ECM, in [EISPlot.py](eis/EISPlot.py). If you'd like to investigate the ECM source code, and perhaps register a new circuit, see [EquivalentCircuitModels.py](eis/EquivalentCircuitModels.py).

Example notebooks:

- [eis_plot_and_ecm_fit_examples.ipynb](notebooks/eis_plot_and_ecm_fit_examples.ipynb).
  - Examples of inspecting the EIS data, creating ECMs from it
- [eis_ecm_guess_scoring_correct_ECM.ipynb](notebooks/eis_ecm_guess_scoring_correct_ECM.ipynb).
  - Examples of scoring parameter guesses and fitting parameters when you've got the correct ECM
- [eis_ecm_guess_scoring_wrong_ECM.ipynb](notebooks/eis_ecm_guess_scoring_wrong_ECM.ipynb).
  - Examples of scoring parameter guesses and fitting parameters when you've got the wrong ECM

## EIS Data Files

The EIS data for training and validating your model(s) has been provided to you in [train_data.csv](train_data.csv). This data file contains rows of EIS data with Frequencies, Impedances, QuantumScape identified ECM classes, and QuantumScape optimized ECM parameters. This consists of 7462 rows of already-labeled EIS data provided by QuantumScape.

We also have a dataset of never-labeled EIS data, [unlabeled_data.csv](unlabeled_data.csv). This data file contains 18569 rows of unlabeled EIS spectra provided by QuantumScape.

An example of the format we're expecting for the challenge submission is provided at [submission_example.csv](submission_example.csv), and the [Challenge Description](Challenge.md) has more wordy detail on the format. It's generated as simple copy from the Circuit and Parameters columns of training data file.

## Environments

All this python code and tooling has dependencies which are encoded in the environment files. We've set up support for [Anaconda](https://anaconda.org/), [Poetry](https://python-poetry.org/), and [Docker](https://www.docker.com/) environments. Even if you're not primarily using python for your development, we encourage you to setup a python environment just to use DVC and our scoring ClI (see next section). If you are using another programming language, please provide details on your environment in one of the commonly accepted formats, and a brief description of how to set it up.

To install the anaconda environment, you need to have anaconda installed, then run:

```shell
conda env create --file environments/environment.yml
cp environments/pyproject.toml .
pip install .
```

To install the poetry environment, you need to have python 3.10 or higher installed, then run:

```shell
cp environments/pyproject.toml .; poetry install
```

To install the Docker environment, you need to have Docker installed, then run:

```shell
cp environments/docker-compose.yml .
cp environments/Dockerfile .
cp environments/jupyter.sh .
docker-compose build
```

The Docker container is setup to run a juypter lab server on start. You can start it with `docker-compose up`.

After you picked and setup an environment in your repository, please delete the other environment files so the judges know which one you used when judging the submissions.

## Data Pipelines and Data Version Control (DVC)

In order to facilitate both judging and teamwork, we hope competitors will write easy-to-use data pipelines for their submissions. This could take the form of a single script/notebook, or a collection of scripts/notebooks run in order and reading/writing data from each other. If you're pursuing the latter case (which we recommend), BatteryDEV encourages the use of the Data Version Control tool as a way to improve your quality of life when working with data pipelines.

[DVC](https://dvc.org/) is an open-source tool for data science collaboration, written in python. We recommend using the DVC tooling, as it will make it easier to collaborate with your team. It is language agnostic, and can run scripts or notebooks written in any language as long as they can be executed from the command line and write data to an expected location on disk. It automates caching pipeline stage inputs and outputs, sharing data, detecting if pipeline stages have been affected by upstream changes, and more.

An example of a very basic "machine learning" pipeline has been setup in [example_pipeline](example_pipeline/). See it's [README](example_pipeline/README.md) to get it started.

If you'd like to use different data pipeline tooling, please add it to your environment before submission, and provide as part of your submission some brief description of how to use it - just links to official docs is fine, but any specific advice is appreciated.

## Notebooks

If you're using notebooks in your ML pipeline, please make sure they can be executed in the order the cells are present. This ensures that the notebook can be executed from the command line like so:

```shell
jupyter nbconvert --execute <notebook>
```

One of the reasons we've picked DVC for pipelining is you can run a jupyter notebook as a DVC stage, as long as it outputs data into the file that DVC is expecting. Submitting your entire project as one cleaned-up notebook is also acceptable.

## Using Other Languages

We encourage competitors to use another open-source programming language to build their ML pipelines. We did not have time to setup the EIS utility library and environments in those languages! Sorry! If you do write scripts/tools in other languages, please include the commands to run them in the DVC pipeline - it is totally agnostic to the underlying language of the commands it runs! Doing so will help the judges assess your submission.

# QuantumScape Dataset Challenge

This document provides a general overview of the data sets, problems to tackle, and submission expectations for the QuantumScape data challenge. For an overview of the more technical setup, expectations, and tools provided, see the [README](README.md)

## Data Description

10,000-ish Electrical Impedance Spectroscopy (EIS) spectra provided by QuantumScape, with Equivalent Circuit Models (ECM) identified, with good parameters defined. Additionally, 18,500-ish EIS spectra provided by QuantumScape that are unlabeled.

## Background

EIS data is used as a source of diagnostic information across the battery industry. However, in many cases, for EIS data to be useful, ECMs need to be fit to the data with reasonable (i.e. physically possible) parameters. These ECMs can then be used in combination with the EIS data to diagnose specific issues in the batteries tested.

## Challenge

To automate the classification of appropriate ECMs given a EIS dataset similar to the ones provided by QS. In addition, if possible, to automate good guesses for ECM parameters. This guess at the parameters doesn’t need to yield a perfect fit, but be a good initial starting point for a more traditional parameter optimization. Provided a correct ECM type, and a good initial guess for the parameters, fitting the EIS data is quite straightforward – you’ll find we’ve gone ahead and implemented a basic version of the parameter fitting for you already.

## Challenge Tasks

We’ve defined for this challenge two scoring metrics- the first is a standard classification metric, the second is a somewhat odd regression metric. A part of the judging will be qualitative and done by experts in ML and EIS, however, so we welcome creative extensions that exceed the parameters of these metrics, or alternative ways of solving the background issue that skip them entirely.

### Classification of ECM Classes

Create a model that can predict the ECM class in the test dataset as accurately as possible. Measured via a standard multiclass balanced accuracy.

- A Possible Extension Idea
  - Create a generative model to propose ECM classes for an EIS curve, possibly including classes not in the dataset already.

### Regression for ECM Parameters Guesses

Estimate best-fit circuit parameters in the test dataset as accurate as possible. Measured via a custom cross-validated loss after parameter optimization using scipy.

- A Possible Extension Idea
  - Build a combined ECM-circuit classification and parameter guessing model that provides reasonable parameter guesses for multiple ECM models, for the same EIS spectrum.

### Submission

Your submission for judging should be entirely contained within this repository. We expect a data file of the simple format found in [submission_example.csv](submission_example.csv). The rows in your submission should correspond to the rows in [test_data.csv](test_data.csv) - so line 2 on the submission is the predictions for line 2 of test data, line 3 of the submissions is the predictions for line 3 of the test data, and so on. The example submission data was generated from the training data set, and row-matches it as described.

If you've just provided a circuit class guess for a line, and no parameters guess, please just leave the `Parameters` column blank for that row.

The repository upon submission should contain the MIT license, and not use any closed-source tools. Please replace the generic author text in [the license](LICENSE) with the names of your team members.

### A Creative Solutions Idea

Define a way of scoring an ECM class and/or parameters against an EIS spectrum that can determine how appropriate an ECM class is for this EIS spectrum, without reference against similarity to already-labeled data.

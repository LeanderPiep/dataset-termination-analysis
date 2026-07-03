# Dataset for Program Slicing and Termination Analysis

This repository contains two datasets for evaluating program analysis tasks:

1. Program Slicing Dataset  
2. Termination Analysis Dataset  

---

## Program Slicing Dataset

The dataset consists of 40 Python scripts designed to evaluate the extraction of relevant program context.

Characteristics:
- Script length ranges from 13 to 58 lines of code
- Multiple functions with direct and transitive dependencies
- Use of global variables

Each script contains exactly one target function. The task is to extract a program slice that includes all referenced functions and relevant global variables.

---

## Termination Analysis Dataset

This dataset is based on the HaltEval dataset by Meta and contains 230 Python programs.

Original dataset:
https://github.com/facebookresearch/halteval

The programs have been extended to include:
- Additional functions
- Global variables
- Inter-function dependencies

These modifications aim to reflect more realistic program structures.

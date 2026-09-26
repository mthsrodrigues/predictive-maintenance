# Predictive Maintenance with NASA C-MAPSS

Machine Learning Engineering project for estimating the **Remaining Useful Life (RUL)** of turbofan engines using the NASA C-MAPSS dataset.

The goal is not only to train a model, but to transform a Data Science experiment into an organized, testable, and reproducible ML application with an API, Docker, and continuous integration.

## Problem

In predictive maintenance, an important question is how much longer a piece of equipment can operate before reaching a failure condition.

In this project, the problem is formulated as a regression task:

> Given the operating conditions and sensor readings of an engine at a specific cycle, estimate its remaining useful life.

The target variable is the **Remaining Useful Life (RUL)**.

## Dataset

This project uses the **NASA C-MAPSS** dataset, specifically the **FD001** subset.

The dataset contains simulated engine degradation trajectories.

Each observation includes:

- engine identifier;
- operation cycle;
- operating settings;
- sensor readings.

In the training set, each engine trajectory continues until failure. Therefore, RUL can be calculated as:

```text
RUL = last cycle of the engine - current cycle
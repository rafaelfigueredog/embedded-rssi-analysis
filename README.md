# Analysis of 5G Signal

Exploratory Analysis of 5G Signal Power

## Overview

This repository contains the code and data files used for conducting an exploratory analysis of 5G signal power. The study is part of a master's degree research project at the Federal University of Campina Grande. The goal of the analysis is to investigate the signal power variations in different positions using JSON data files.

## File Structure

The repository has the following file structure:

```
.
├── analysis
│   └── data-visualization.ipynb
├── data
└── scripts
    └── main.py
```

The `analysis` directory contains the Jupyter Notebook `data-visualization.ipynb`, which contains the code for visualizing the data. The `data` directory contains JSON files, each representing the signal power data for a specific position. The `scripts` directory contains the `main.py` file, which is a script for collect the data.

## Data Format

Each JSON file in the `data` directory follows the structure below:

```json
[
    {
        "ssid": "NOKIA-402343AC9C25-5",
        "quality": "70/70",
        "signal": -21,
        "mac": "40:23:43:AC:9C:32"
    },
    {
        "ssid": "NOKIA-402343AC9C25-5",
        "quality": "70/70",
        "signal": -25,
        "mac": "40:23:43:AC:9C:32"
    },
    ...
]
```

The JSON file contains an array of objects, where each object represents a signal reading. Each reading includes information such as SSID, signal quality, signal strength, and MAC address.

## Usage

To analyze the data and visualize the results, follow these steps:

1. Ensure that Python and the required libraries (such as pandas, seaborn, and matplotlib) are installed in your environment.
2. Clone this repository to your local machine.
3. Navigate to the `analysis` directory.
4. Open the `data-visualization.ipynb` Jupyter Notebook.
5. Run the notebook cells to load and process the data, generate visualizations, and perform exploratory analysis.

## Results

The analysis performed using the provided code and data files aims to explore the variations in 5G signal power across different positions. The generated visualizations help to understand the relationship between signal power, position, and signal quality. The results of the analysis contribute to the ongoing research project for the master's degree at the Federal University of Campina Grande.

## Acknowledgments

We would like to express our gratitude to the Federal University of Campina Grande for supporting this research project and providing the necessary resources and infrastructure. Special thanks to the research advisors and collaborators for their guidance and assistance throughout the study.

## Contact

For any questions or inquiries, please contact:

Rafael Guimarães, (rafaelguimaraes@copin.ufcg.edu.br) <br />
Federal University of Campina Grande

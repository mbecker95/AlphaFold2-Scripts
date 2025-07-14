#!/usr/bin/python
"""
File: af2_heatmap.py
Author: Mark H. Becker
Date: 2025-07-14
Description: A Python script for outputting predicted aligned error heatmaps for AlphaFold models.
"""

# 1.  Importing all of the appropriate modules for data interpretation and plotting

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob as glob
import os
import seaborn as sns

# 2.  Obtaining the names of all of the pickle files and the directory of the outputs

files = glob.glob('result*.pkl', recursive=True)
dir_name = os.getcwd().split('/')[-1]

# 3a. Stripping the predicted alignment error, pTM and ipTM from the pickle files for each model.
# 3b. Using the stripped data to plot the predicted alignment error while outputting the other parameters

for file in files:
    df = pd.read_pickle(file) # add different models
    plt.figure(figsize=([10,8]))
    sns.heatmap(df['predicted_aligned_error'],cmap='viridis')
    ptm = np.round(df['ptm'],2)
    iptm = str(np.round(df['iptm'],2)) if 'iptm' in df else False
    name = []
    file.split('_')
    name.append(file.split('_')[1])
    name.append(file.split('_')[2])
    model_name = ' '.join(name)
    file_model_name = '_'.join(name)
    if iptm == False:
        plt.title(f"protein: {dir_name}, {model_name}, pTM: {ptm}")
    else:
        plt.title(f"protein: {dir_name}, {model_name}, pTM: {ptm}, ipTM: {iptm}")
    plt.savefig(f'{dir_name}_{file_model_name}.png')

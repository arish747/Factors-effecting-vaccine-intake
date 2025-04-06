import numpy as np
import pandas as pd
import seaborn as sns
# import torch
import matplotlib.pyplot as plt
import math
import machine_learning_datasets
import ml_datasets
import statsmodels.api as sm
# import statsmodel.api as sm
from sklearn.model_selection import train_test_split

cvs_df = pd.read_csv(r'C:\Users\arish\OneDrive\Desktop\analytic_data2020_0.csv', header= 1)

cvs_df.info()
cvs_df.describe()


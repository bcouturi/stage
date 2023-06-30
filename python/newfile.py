# import everything i'll need
import mplhep
import uproot
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import auc, roc_curve
from sklearn.model_selection import KFold
from xgboost import XGBClassifier

# old program
my_file = uproot.open("real_data.root")
my_file.keys()
tree = my_file["DecayTree"]
data_df = tree.arrays(library="pd")
data_df
vbkg_df = data_df.query("~(3.0 < Jpsi_M < 3.2)")
# create a scatter graph
plt.scatter(mc_df["mup_PT"], mc_df["mum_PT"], s=1, marker=",", label="Signal")
plt.scatter(bkg_df["mup_PT"], bkg_df["mum_PT"], s=1, marker=",", label="Background")
plt.xlabel("mup_PT")
plt.ylabel("mum_PT")
plt.legend()

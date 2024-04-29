
#Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#Create dictionary with organization data
org_data = {
    "Organization" : ["Red Cross", "Salvation Army", "Feeding America", "Direct Relief", "Goodwill"],
    "Donations (Millions of Dollars)" : [500, 300, 200, 100, 150],
    "Volunteers" : [100, 50, 75, 25, 100],
    "Program Expenses (%)" : [75, 80, 70, 85, 60],
    "Administrative Expenses (%)" : [10, 15, 20, 10, 25],
    "Fundraising Expenses (%)" : [15, 5, 10, 5, 15],
    "Impact Score" : [93, 90, 87, 92, 85]
}

#Convert dictionary to pandas dataframe
df = pd.DataFrame(org_data)

#Set figure size
plt.figure(figsize=(10,8))

#Plot heatmap using sns.heatmap()
ax = sns.heatmap(df.iloc[:,1:], annot=True, fmt=".0f", cmap="Blues", annot_kws={"size": 12})

#Format ticks and labels
ax.set_xticklabels(df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df["Organization"], rotation=0, ha="right", rotation_mode="anchor")

#Add title
plt.title("Nonprofit Performance Metrics")

#Resize and save image
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-163105_3.png", bbox_inches="tight")

#Clear state
plt.clf()
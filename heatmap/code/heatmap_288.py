import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data processing
data = {'Sport': ['Football','Basketball','Baseball','Soccer','Hockey'],
        'Attendance': [70,50,40,30,20],
        'Revenue (Millions)': [500,400,300,200,100],
        'Merchandise Sales (Millions)': [50,40,30,20,10],
        'TV Viewership (Millions)': [500,400,300,200,100],
        'Social Media Followers (Millions)': [100,80,60,40,20],
        'Team Value (Millions)': [1000,800,600,400,200]}

df = pd.DataFrame(data, columns = ['Sport', 'Attendance', 'Revenue (Millions)', 'Merchandise Sales (Millions)', 'TV Viewership (Millions)', 'Social Media Followers (Millions)', 'Team Value (Millions)'])

# plot the chart
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(df.iloc[:, 1:], annot=True, fmt=".0f", cmap="Blues", cbar=False, ax=ax)
ax.set_title("Sports and Entertainment Metrics", fontsize=14)
ax.set_xticklabels(df.iloc[:, 1:].columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df["Sport"], rotation=0)
ax.tick_params(axis='both', which='major', pad=10)
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-163105_24.png", bbox_inches="tight", pad_inches=0.5)
plt.clf()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# create dictionary using given data
data_dict = {"Category": ["Professional Teams", "Collegiate Teams", "Individual Sports", "E-sports", "Music", "Movies", "Television", "Live Events", "Gaming", "Others"],
            "Football (Fans)": [500000, 250000, 100000, 75000, 300000, 200000, 150000, 100000, 50000, 25000],
            "Basketball (Fans)": [400000, 200000, 80000, 60000, 240000, 160000, 120000, 80000, 40000, 20000],
            "Baseball (Fans)": [300000, 150000, 60000, 45000, 180000, 120000, 90000, 60000, 30000, 15000],
            "Soccer (Fans)": [200000, 100000, 40000, 30000, 120000, 80000, 60000, 40000, 20000, 10000],
            "Hockey (Fans)": [100000, 50000, 20000, 15000, 60000, 40000, 30000, 20000, 10000, 5000]}

# convert first column to string type
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.iloc[:, 1:].columns)

# set x and y axis ticks and ticklabels
if np.random.choice([0, 1], p=[0.3, 0.7]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha="right", rotation_mode="anchor")
if np.random.choice([0, 1], p=[0.3, 0.7]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    if max_total_value > 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    elif max_total_value > 100:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(ax.get_yticks(), rotation=0, ha="right", rotation_mode="anchor")

# set colors and transparency
colors = ['#FFA07A', '#87CEFA', '#90EE90', '#FFDAB9', '#ADD8E6']
for idx, patch in enumerate(ax.patches):
    patch.set_facecolor(colors[idx % 5])
    patch.set_alpha(0.7)

# set background grid lines
ax.grid(axis='y', linestyle='dotted')

# set legend position
ax.legend(loc='upper right')

# set title
ax.set_title("Sports and Entertainment Audience Distribution")

# resize image and save
fig.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-155112_41.png", bbox_inches='tight')

# clear current image state
plt.clf()
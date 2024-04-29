
#import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#represent data using dictionary
data = {"Category": ["2017", "2018", "2019", "2020", "2021"], "Physics (Publications)": [500, 550, 600, 650, 700], "Chemistry (Publications)": [450, 500, 550, 600, 650], "Biology (Publications)": [300, 350, 400, 450, 500], "Computer Science (Publications)": [250, 300, 350, 400, 450], "Engineering (Publications)": [400, 450, 500, 550, 600]}

#convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

#plot the data with the type of area chart
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.stackplot(df["Category"], df["Physics (Publications)"], df["Chemistry (Publications)"], df["Biology (Publications)"], df["Computer Science (Publications)"], df["Engineering (Publications)"], colors=["lightcoral", "khaki", "lightgreen", "skyblue", "plum"], alpha=0.7)

#set x and y axis ticks and ticklabels
if np.random.choice([0, 1], p=[0.3, 0.7]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df["Category"], rotation=45, ha="right", rotation_mode="anchor")
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value > 1000:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    elif max_total_value > 100:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(ax.get_yticks())
else:
    ax.set_xticks([])
    ax.set_yticks([])

#set background grid lines
ax.grid(axis="y", color="lightgray", linestyle="--", linewidth=0.5)

#adjust legend's position
ax.legend(["Physics", "Chemistry", "Biology", "Computer Science", "Engineering"], loc="upper left", bbox_to_anchor=(1, 1))

#automatically resize the image
plt.tight_layout()

#add title and labels
plt.title("Publications by Scientific Category from 2017 to 2021")
plt.ylabel("Number of Publications")

#save the image
plt.savefig("output/final/area_chart/png/20231228-131755_44.png", bbox_inches="tight")

#clear the current image state
plt.clf()
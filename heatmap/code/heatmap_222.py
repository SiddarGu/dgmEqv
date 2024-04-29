


# import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Read data and process into a dictionary
data = "Category,Security,Cybersecurity,Cloud Computing,Internet of Things,Artificial Intelligence\nSoftware,20,30,15,18,25\nHardware,25,20,10,12,8\nServices,15,22,30,28,20\nNetworking,10,8,12,15,10\nTelecommunications,20,20,15,20,22\nE-commerce,10,10,8,7,15\nAnalytics,5,5,10,10,10"
data = data.splitlines()
header = data[0].split(",")
data_dict = {}
for i in range(1, len(data)):
    row = data[i].split(",")
    data_dict[row[0]] = {}
    for j in range(1, len(row)):
        data_dict[row[0]][header[j]] = int(row[j])

# Convert dictionary to dataframe
df = pd.DataFrame.from_dict(data_dict)

# Set figure size and create subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot heatmap using seaborn
sns.heatmap(df, annot=True, cmap="Blues", ax=ax)

# Set x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_yticklabels(df.index, rotation=0, ha="center")

# Add colorbar
cbar = ax.collections[0].colorbar
cbar.set_ticks(np.arange(0, 31, 5))
cbar.set_ticklabels(np.arange(0, 31, 5))
cbar.ax.tick_params(labelsize=12)

# Set title and axis labels
ax.set_title("Technology and Internet Penetration by Category")

# Automatically resize image and save
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/heatmap/png_train/heatmap_222.png", bbox_inches="tight")

# Clear current image state
plt.clf()
plt.close()
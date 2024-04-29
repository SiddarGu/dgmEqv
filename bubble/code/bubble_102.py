import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.colors as mcolors

# Create dataframe from data
data=pd.DataFrame({
    "Platform": ["Facebook","Instagram","Twitter","LinkedIn","Snapchat","Pinterest","TikTok","YouTube","WhatsApp","WeChat"],
    "Number of Users (Millions)": [2200,1000,330,310,280,250,900,2000,2200,1100],
    "Daily Usage (Hours)": [2.5,2,1.5,1,1,1,1.5,2,2,1.5],
    "Advertising Revenue (Billion $)": [40,20,10,12,8,6,15,30,10,8],
    "Engagement (Score)": [8,7,6,7,6,5,8,9,8,9],
    })

# Split dataframe into variables
data_labels = data.columns[1:].tolist()
line_labels = [f"{row['Platform']} ({row[data_labels[2]]})" for _, row in data.iterrows()]
data = data[data_labels].to_numpy() 

# Normalize color and size data
norm = mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
sizes = 600 + (data[:,2] - data[:,2].min()) / (data[:,2].max() - data[:,2].min()) * 4400

# Create figure and add subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

# Plot data
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], c=[plt.cm.jet(norm(data[i, 3]))], s=sizes[i], label=None)
    ax.scatter([], [], c=plt.cm.jet(norm(data[i, 3])), label=line_labels[i])

# Add a color bar
colorbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=plt.cm.jet))
colorbar.set_label(data_labels[3])

# Adjust plot
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2], loc='upper left')
fig.tight_layout()
fig.subplots_adjust(right=0.8)

# Add title and save figure
plt.title('Social Media and Web Metrics 2023')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/333_202312311429.png')

# Clear the current image state
plt.clf()

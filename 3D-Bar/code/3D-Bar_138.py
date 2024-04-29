import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

raw_data = ["Platform,Active Users (in billions),Daily Time Spent (minutes),Monthly Active Users (in billions)",
            "Facebook,28,58,26",
            "YouTube,20,40,23",
            "WhatsApp,20,30,16",
            "Instagram,12,53,10",
            "Twitter,4,33,33"]

transformed_data = [line.split(',') for line in raw_data]
y_values = transformed_data[0][1:]
x_values = [item[0] for item in transformed_data[1:]]
data = np.array([[np.float32(item) for item in sublist[1:]] for sublist in transformed_data[1:]])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.4, 0.5, data[:, i], alpha=0.5, color=np.random.rand(3,))
    
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')
plt.title("Social Media Platforms' Usage Statistics")

ax.view_init(elev=30., azim=-135) # This adjusts the viewing angle
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/144_202312302235.png')
plt.clf()

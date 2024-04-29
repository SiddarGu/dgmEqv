import matplotlib.pyplot as plt
import numpy as np

# data
data_str = """Facebook,1500,2500,70.7 
Instagram,500,1000,20 
Twitter,330,500,3.72 
LinkedIn,260,675,6.8 
Snapchat,280,498,1.7"""

# transform data into lists
rows = data_str.split("\n")
x_values = [row.split(",")[0] for row in rows]
y_values = ["Daily Active Users (Millions)", "Monthly Active Users (Millions)", "Annual Revenue ($Billion)"]
data_values = np.array([list(map(float, row.split(",")[1:])) for row in rows])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# plot data
for i in np.arange(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i] * len(x_values), np.zeros(len(x_values)),
             0.4, 0.5, data_values[:, i], alpha=0.8)
    
# label and tick settings
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# view setting
ax.view_init(elev=20, azim=-45)
ax.set_title('Social Media Usage and Revenue Data')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/157_202312302235.png', format='png')
plt.clf()

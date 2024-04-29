import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the data
orig_data = "Quarter,Revenue (Million $),Expenditure (Million $),Profit (Million $)\n Q1,200,150,300\n Q2,220,170,350\n Q3,250,180,370\n Q4,270,200,400"
lines = orig_data.split("\n")
fields = lines[0].split(",")
x_values = [line.split(",")[0] for line in lines[1:]]
y_values = fields[1:]
data = np.array([list(map(np.float32, line.split(",")[1:])) for line in lines[1:]])

# Create the figure and a 3D subplot
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

# Create the 3D bar chart
_x = np.arange(len(x_values))
_y = np.arange(len(y_values))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

bottom = np.zeros_like(data.flatten())
width = depth = 1
top = data.flatten()

ax.bar3d(x, y, bottom, width, depth, top, shade=True, color='b', alpha=0.6)

# Customise the labels and view
ax.set_xlabel('Quarters')
ax.set_ylabel('Financial Performance Metrics')
ax.set_zlabel('Million $')
ax.set_xticks(_x)
ax.set_yticks(_y)
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticklabels(y_values, ha ='left')
ax.view_init(azim=60)

# Set up the title and save the figure
plt.title("Company's Quarterly Financial Performance in a Fiscal Year")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/234_202312310050.png')

# Clears the current figure
plt.clf()

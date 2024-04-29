import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
csv= "Organization,Donation Collected ($000),Number of Beneficiaries,Annual Expenditure ($000)\nSave The Children,3500,7000,3000\nDoctors Without Borders,3000,6000,2500\nAmerican Cancer Society,4000,8000,3500\nHabitat for Humanity,2800,6500,2400\nSalvation Army,3600,7500,3080"
rows = csv.split("\n")
x_values = [row.split(",")[0] for row in rows[1:]]
y_values = rows[0].split(",")[1:]
data = np.array([list(map(float, row.split(",")[1:])) for row in rows[1:]], dtype=np.float32)

# Figure creation
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Draw bars
for i, y in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), [i] * len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], color='b', alpha=0.5)

# Rotate axis labels and setting ticks
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, wrap=True)
ax.set_yticklabels(y_values, ha='left')

# Set viewing angle and title
ax.view_init(elev=20., azim=-35)
plt.title('Annual Overview of Major Charity and Nonprofit Organizations')

# Auto resize and save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/130_202312302126.png')
plt.cla()
plt.close(fig)

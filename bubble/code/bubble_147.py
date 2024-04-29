import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
import io

# Read data
data = """Department,Number of Employees,Employee Satisfaction Score (%),Average Annual Salary ($),Employee Retention Rate (%)
HR,120,89,80000,95
Finance,200,84,90000,90
Marketing,140,78,85000,85
Sales,210,95,90000,98
Operations,250,86,75000,92
IT,180,90,100000,90
Administration,100,80,70000,88"""
data = pd.read_csv(io.StringIO(data))

# Transform into the required format
line_labels = [f"{row.Department} {row['Employee Retention Rate (%)']}" for idx, row in data.iterrows()]
data_labels = data.columns[1:]
data = data.drop(columns='Department').to_numpy()

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define color map
cmap = get_cmap("viridis")
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))

# Plot the data
for i in range(len(line_labels)):
    ax.scatter(data[i, 0], data[i, 1], c=[cmap(norm(data[i, 3]))], s=data[i, 2]/ 20,
               label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_labels[i])

# Add legend and labels
ax.legend(title=data_labels[2])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Add a colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])

# Set the title
plt.title("Analysis of Employee Management Metrics for Every Department")

# Save the image
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/214_202312310045.png")

# Clear the current image state
plt.clf()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data
y_values = ['Physics Graduates', 'Chemistry Graduates', 'Computer Science Graduates', 'Engineering Graduates']
dataset = [['2017',650,780,850,900],
           ['2018',670,800,865,905],
           ['2019',690,820,880,910],
           ['2020',710,840,895,920],
           ['2021',730,860,910,930]]
x_values = [row[0] for row in dataset]
data = np.array([row[1:] for row in dataset], dtype=np.float32)

# Create Figure and Subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Adjust viewing angle
ax.view_init(30, -135)

# Set bar widths and depths
bar_width = 0.8
bar_depth = 0.8

# Iterate over y_values to plot each column of data
for i, y_value in enumerate(y_values):
    ax.bar3d(
        np.arange(len(x_values)), 
        [i]*len(x_values), 
        np.zeros(len(x_values)),
        bar_width, bar_depth, data[:, i],
        shade=True, color=['r', 'g', 'b', 'c'][i % 4], alpha=0.6)

# Set title and labels
ax.set_title("The Number of Graduates in Key Fields of Science and Engineering from 2017 to 2021")
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Automatically adjust subplot params so that the subplot(s) fits in to the figure area.
fig.tight_layout()

# Save the figure as a png file
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/279_202312310050.png')

# Clear the current figure.
plt.clf()

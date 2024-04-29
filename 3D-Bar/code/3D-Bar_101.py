
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
y_values = ['Number of Cases Filed (Thousands)', 'Number of Cases Resolved (Thousands)', 'Number of Judgements (Thousands)']
data = np.array([[20, 15, 12], [30, 28, 25], [10, 8, 7], [5, 4, 3]])
x_values = ['Civil Law', 'Criminal Law', 'Administrative Law', 'Constitutional Law']

# Plot the data with the type of 3D bar chart
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values),
             np.zeros(len(x_values)), 0.5, 1, data[:, i], shade=True, color='red', alpha=(i + 1) * 0.2)

# Set the dimensions of the bars
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xlabel('Type of Law')
ax.set_xticklabels(x_values, rotation=60)
ax.set_yticklabels(y_values)

# Drawing techniques such as background grids can be used
ax.grid(False)
ax.set_title('Legal System Performance - Case Filing, Resolution and Judgement Statistics')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/41_202312270030.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/41_202312270030.png')

# Clear the current image state at the end of the code
plt.clf()
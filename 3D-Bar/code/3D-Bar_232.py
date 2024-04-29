
import matplotlib.pyplot as plt
import numpy as np

# Split data into y_values and data
y_values = ['Robotics Research (USD Billion)', 'Aerospace Research (USD Billion)', 'Biomedical Research (USD Billion)', 'Computer Science Research (USD Billion)']
data = np.array([[1.2, 2.6, 3.4, 4.2], [1.7, 3.2, 4.1, 5.0], [2.2, 3.8, 4.9, 5.9], [2.7, 4.4, 5.4, 6.4], [3.2, 5.0, 6.2, 7.2]])
x_values = ['2019', '2020', '2021', '2022', '2023']

# Create figure and subplot
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(xs)), 0.8, 0.8, data[:, i], shade=True)

# Set the dimensions of the bars and labels
ax.set_xlabel('Year')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Title of the figure
ax.set_title('Science and Engineering Research Expenditure - 2019 to 2023')

# Automatically resize the image and savefig
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/24_202312251044.png')

# Clear the current image state
plt.clf()
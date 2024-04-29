
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
y_values = ['Average Test Score (%)', 'Average Homework Score (%)', 'Average Class Participation Score (%)', 'Average Final Grade (%)']
data = np.array([[85, 90, 95, 90], [80, 85, 90, 85], [75, 80, 85, 80], [70, 75, 80, 75], [65, 70, 75, 70], [60, 65, 70, 65]])
x_values = ['Kindergarten', '1st Grade', '2nd Grade', '3rd Grade', '4th Grade', '5th Grade']

# Create figure before plotting
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    bottom = np.zeros(len(x_values))
    width = 0.7
    depth = 0.5
    # Plot the data with the type of 3D bar chart
    ax.bar3d(xs, ys, bottom, width, depth, data[:, i], shade=True, color=plt.cm.Spectral(i/len(y_values)))

# Set the dimensions of the bars
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Set the title of the figure
ax.set_title('Academic Performance of Students - Kindergarten to 5th Grade')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/22_202312270030.png')

# Clear the current image state at the end of the code
plt.clf()
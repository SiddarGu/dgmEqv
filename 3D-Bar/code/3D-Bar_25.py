

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: y_values, data, x_values. 
y_values = ['Number of Criminal Cases (Thousands)', 'Number of Civil Cases (Thousands)', 'Number of Family Cases (Thousands)']
data = np.array([[1200, 4000, 3000], [1300, 4200, 3200], [1400, 4400, 3400], [1450, 4500, 3500], [1500, 4600, 3600]])
x_values = ['2015', '2016', '2017', '2018', '2019']

# Create figure before plotting
fig = plt.figure(figsize=(15, 6))
ax = fig.add_subplot(111, projection='3d')

# Plotting the data
for i, y in enumerate(y_values):
    xpos, ypos = np.meshgrid(np.arange(len(x_values)), [i])
    xpos = xpos.flatten()
    ypos = ypos.flatten() - 0.5
    zpos = np.zeros(len(x_values))
    dx = 0.3 * np.ones(len(x_values))
    dy = 0.3 * np.ones(len(x_values))
    dz = data[:, i]

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True, color=plt.cm.jet(i/len(y_values)), alpha=0.6)

# Rotate the X-axis labels for better readability
x_range = np.arange(len(x_values))
ax.set_xticks(x_range)
ax.w_xaxis.set_ticklabels(x_values, rotation=30)
ax.set_xlabel('Year')
y_range = np.arange(len(y_values))
ax.set_yticks(y_range)
ax.w_yaxis.set_ticklabels(y_values, ha='left')
ax.set_ylabel('Metrics')

# Drawing techniques such as background grids can be used
ax.grid(True)
# Set the title of the figure
ax.set_title('Legal Cases Overview - 2015 to 2019', pad=20)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/20.png')

# Clear the current image state
plt.clf()
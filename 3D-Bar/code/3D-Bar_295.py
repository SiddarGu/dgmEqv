
import numpy as np
import matplotlib.pyplot as plt

# Transform data into three variables
y_values = ["Enrollment (Millions)", "Dropout Rate (%)", "Graduation Rate (%)", "Tuition Fees ($000)"]
x_values = ["2015", "2016", "2017", "2018", "2019"]
data = np.array([[17.2, 7.4, 83.9, 24.8], [17.4, 8.2, 84.6, 26.2], [17.6, 8.3, 84.5, 27.8], [17.9, 8.1, 83.7, 29.1], [18.1, 7.9, 83.2, 30.5]])

# Create figure before plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Iterate y_values to plot each column of data
for i in range(len(y_values)):
    xpos = np.arange(len(x_values)) 
    ypos = [i] * len(x_values)
    xpos = xpos + 0.2
    colors = ['b','g','r','y']
    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), 0.4, 0.3, data[:,i], color=colors[i], alpha=0.5)

# Set the dimensions of the bars
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)

# Drawing techniques such as background grids can be used
ax.grid(b=True, which='major', color='k', linestyle='--', alpha=0.2)

# Add title
ax.set_title("Trends in Education and Academics - 2015 to 2019")

# Resize image by tight_layout()
fig.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/10_202312270030.png')

# Clear the current image state
plt.cla()
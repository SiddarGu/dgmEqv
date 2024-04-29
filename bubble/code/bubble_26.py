
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform the given data into three variables
data_labels = ["Grades (GPA)", "Test Scores (%, A-F)", "Enrollment (Number)", "Course Load (Hours)"]
data = np.array([[3.2, 90, 1000, 16],
                [3.5, 92, 900, 17],
                [3.7, 95, 850, 18],
                [3.9, 97, 800, 19],
                [4.0, 99, 750, 20]])
line_labels = ["Freshman", "Sophomore", "Junior", "Senior", "Graduate"]

# Plot the data with the type of bubble chart
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot()

for i in range(len(line_labels)):
    # scatter an empty point
    ax.scatter([], [], label=line_labels[i], s=20, color=cm.jet(Normalize(15, 20)(data[i, 3])))
    # plot the data
    ax.scatter(data[i, 0], data[i, 1], s=Normalize(700, 1000)(data[i, 2]) * 5000 + 600, label=None, color=cm.jet(Normalize(15, 20)(data[i, 3])))

# plot the legend with the title
ax.legend(title=data_labels[2], fontsize="large")

# add a color bar
sm = cm.ScalarMappable(cmap=cm.jet, norm=Normalize(vmin=15, vmax=20))
sm.set_array([])
plt.colorbar(sm, ax=ax, label=data_labels[3])

# set labels, title, background grid
ax.set_title("Student Performance and Academic Load - Education 2023")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)

# resize the image
plt.tight_layout()

# save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/16_2023122261326.png")

# clear the current image state
plt.clf()
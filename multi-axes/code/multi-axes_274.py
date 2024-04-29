import numpy as np
import matplotlib.pyplot as plt

# Process the data string
data_string = "Scientific Discipline,Number of Graduates (Thousands),Employment Rate (%),Average Starting Salary (Thousands of Dollars)\n Computer Science,216,98,72\n Engineering,120,90,68\n Physics,25,95,55\n Mathematics,40,96,67\n Chemistry,75,92,51\n Environmental Science,30,89,45\n Astronomy,7,93,61\n Geography,60,88,42\n Geology,20,97,59\n Biology,220,89,48"

lines = data_string.split("\n")
header = lines[0].split(",")
data_labels = header[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = np.array([line.split(",")[1:] for line in lines[1:]], dtype=float)

# Create the figure
fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax3 = ax1.twinx()

# Adjust the position of the extra axis
ax3.spines['right'].set_position(('axes', 1.1))

# Plot the data
ax1.bar(line_labels, data[:, 0], color='g', alpha=0.7, label=data_labels[0])
ax2.scatter(line_labels, data[:, 1], color='b', label=data_labels[1])
ax3.plot(line_labels, data[:, 2], color='r', label=data_labels[2])

# Set the axis labels
ax1.set_ylabel(data_labels[0], color='g')
ax2.set_ylabel(data_labels[1], color='b')
ax3.set_ylabel(data_labels[2], color='r')

# Set the title
plt.title("Science and Engineering Graduates: Statistics on Employment and Salary")

# Show the legends
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
ax3.legend(loc="center right")

# Set the grid
ax1.grid(True)

# Save the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/246_202312311051.png")

# Clear the current figure
plt.clf()

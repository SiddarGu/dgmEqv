
import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Number of Users (Millions)", "Average Revenue per User (Dollars)", "Revenue (Millions of Dollars)"]
data = np.array([[1.2, 100, 120], [2.8, 50, 140], [2.3, 60, 138], [0.9, 150, 135],
                [0.5, 120, 60], [3.6, 75, 270], [2.5, 30, 75], [0.7, 200, 140]])
line_labels = ["Social Media", "Online Shopping", "Cloud Computing", "Big Data",
                "Cyber Security", "Online Advertising", "Mobile Apps", "Artificial Intelligence"]

# Create figure
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot data
ax1.bar(line_labels, data[:,0], label=data_labels[0], color='#6495ED', width=0.5)
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'ro-', label=data_labels[1], color='#FF8C00')
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], 'bs-', label=data_labels[2], color='#00FA9A')

# Adjust the position of ax3
ax3.spines['right'].set_position(('axes', 1.1))

# Label all axes
ax1.set_ylabel(data_labels[0], color='#6495ED')
ax2.set_ylabel(data_labels[1], color='#FF8C00')
ax3.set_ylabel(data_labels[2], color='#00FA9A')

# Adjust the range of all y-axes
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

# Show the legends of all plots
ax1.legend(loc="upper left")
ax2.legend(loc="upper center")
ax3.legend(loc="upper right")

# Set title
plt.title("Technology and the Internet: User Engagement and Revenue Insights")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/12_2023122261325.png')

# Clear the current image state
plt.clf()
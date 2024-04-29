import matplotlib.pyplot as plt
import numpy as np

# Data for the transportation and logistics profitability analysis
y_values = ["Passengers (Million)", "Revenue ($ Billion)", "Distance (Miles)"]
data = np.array([[1.8, 22, 25], [3, 25, 6.5], [3.5, 4.5, 4.5], [2, 15, 10]])
x_values = ["Air", "Rail", "Road", "Water"]

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.8, 0.4, data[:, i], color=plt.cm.jet(i/len(y_values)), alpha=0.6)

# Customizing axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=20, fontsize=10)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, fontsize=10)

# Setting title
ax.set_title("Transportation and Logistics Profitability Analysis", fontsize=16)

# Adjusting layout and saving figure
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/12_202312251000.png")

# Clear the current image state 
plt.clf()
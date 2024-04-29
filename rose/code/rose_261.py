

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Criminal Law','Civil Rights','Corporate Law','Family Law','Labor Law','Intellectual Property','Environmental Law','Tax Law','International Law']

data = [2000,1800,1400,1300,1100,900,700,500,300]

line_labels = ['Category','Number of Cases']

num_categories = len(data_labels)

sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='polar')

for i in range(num_categories):
    # Set the angle for the sector
    angle = sector_angle * i

    # Set the radius for the sector
    radius = data[i]

    # Plot the sector
    ax.bar(angle, radius, width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

# Set the x-axis tick values to the angle of each sector
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set the x-axis tick labels to the labels of each sector
ax.set_xticklabels(data_labels, fontsize=15)

# Adjust the legend position
ax.legend(bbox_to_anchor=(1.2, 0.9))

# Add title
plt.title("Number of Legal Cases by Category in 2021")

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_38.png")

# Clear the current image state
plt.clf()
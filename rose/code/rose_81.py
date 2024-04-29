
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Criminal Law", "Civil Rights", "Corporate Law", "Family Law", "Labor Law", "Intellectual Property", "Environmental Law", "Tax Law", "International Law"]
data = [800, 750, 400, 450, 700, 150, 200, 600, 100]
line_labels = ["Legal Category", "Number of Practitioners"]

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='polar')

# Set the color of each sector
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple']

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the chart
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

# Set the ticks to be the categories
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Add legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Set figure title
plt.title("Number of Legal Practitioners by Field in 2021")

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_56.png")

# Clear the current image state
plt.clf()
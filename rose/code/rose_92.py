
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ["Health","Education","Animal Welfare","Poverty","Human Rights","Environment","Arts","International Aid"]
data = [100,90,75,60,50,45,30,20]
line_labels = ["Category","Number of Organizations"]

# Create figure and polar axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)

# Create rose chart
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, bottom=0.0, label=data_labels[i], color=np.random.rand(3,))

# Set the ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, wrap=True, rotation=90)

# Set legend
ax.legend(bbox_to_anchor=(1.2, 1.0))

# Set title
ax.set_title('Number of Nonprofit Organizations in Each Area', fontsize=20)

# Adjust the margins
fig.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_8.png")

# Clear the current image state
plt.clf()
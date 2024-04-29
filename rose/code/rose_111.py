
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Movies","Music","Sports","Television","Books","Video Games","Social Media","Theatre"]
data = np.array([87,91,95,75,40,60,45,20])
line_labels = ["Category","Number"]

# Create figure
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Set ticks and legend
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=14)

# Set title
ax.set_title("Popularity of Entertainment Media in 2021", fontsize=20)

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-054203_9.png')

# Clear current image state
plt.clf()
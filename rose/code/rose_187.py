
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Painting", "Sculpture", "Photography", "Literature", "Music", "Dance", "Theatre", "Film"]
data = [45, 97, 17, 36, 96, 60, 68, 80]
line_labels = ["Art Form", "Number"]

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Calculate angle of each sector
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw each sector
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i / num_categories))

# Set up labels
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, wrap=True)

# Set up legend
ax.legend(bbox_to_anchor=(1.2, 1.0))

# Set up title
plt.title("Number of Art Forms Practiced in the Arts and Culture Scene")

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_25.png")

# Clear the current image state
plt.clf()
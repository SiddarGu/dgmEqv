
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Painting', 'Sculpture', 'Music', 'Literature', 'Dance', 'Theatre', 'Film', 'Architecture']
data = [27, 97, 17, 36, 96, 60, 68, 25]
line_labels = ['Genre', 'Number']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Set up a figure
fig = plt.figure(figsize=(8, 8))

# Set up a polar axes
ax = fig.add_subplot(111, projection='polar')

# Plot the data
for i, v in enumerate(data):
    ax.bar(sector_angle * i, v, sector_angle, label=data_labels[i], color=plt.cm.Set1(i / num_categories))

# Set up the labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, wrap=True)

# Set up the legend
ax.legend(bbox_to_anchor=(1.25, 1.01), loc="upper right")
ax.set_title('Popularity of Arts and Culture Genres in 2021', fontsize=14)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_82.png')

# Clear the current image state
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

# Transform data into variables
data = np.array([50, 100, 20, 40, 80, 60, 30, 10, 25])
data_labels = ['Music', 'Movies', 'Theater', 'Concerts', 'Sports', 'Video Games', 'Gambling', 'Online Streaming', 'Radio']
line_labels = ['Category', 'Number']

# Plot the data
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Create sectors for each category
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, bottom=0.0, color=plt.cm.Set1(i/num_categories))
    ax.set_xticks([sector_angle * i + sector_angle / 2 for i in range(num_categories)])
    ax.set_xticklabels(data_labels, fontsize=12, rotation = 90, ha="center", va="center")

# Add a legend
ax.legend(data_labels, bbox_to_anchor=(1.2, 1.1))

# Set chart title
plt.title('Number of Entertainment and Sports Activities in 2021')

# Tighten the layout 
plt.tight_layout()

# Save chart
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_38.png')

# Clear figure
plt.clf()
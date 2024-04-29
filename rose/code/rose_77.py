
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Banking', 'Investing', 'Accounting', 'Financial Planning', 'Insurance', 'Real Estate', 'Taxation', 'Wealth Management']
data = [50, 60, 80, 90, 100, 60, 20, 10]
line_labels = ["Financial Category", "Number"]

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Draw the sectors
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=f'C{i}', label=data_labels[i])

# Set the label positions
label_positions = np.arange(num_categories) * sector_angle + sector_angle/2
ax.set_xticks(label_positions)
ax.set_xticklabels(data_labels, fontsize=10, ha='center')

# Set the title and legend
ax.set_title('Overview of Financial Categories in 2021', fontsize=14)
ax.legend(bbox_to_anchor=(1.3, 0.3), labels=data_labels, fontsize=10)

# Adjust the layout to make the legend visible
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_50.png', bbox_inches='tight')

# Clear current image state
plt.clf()
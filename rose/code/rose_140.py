
import matplotlib.pyplot as plt
import numpy as np

# transform data into three variables
data_labels = ["Poultry Production", "Dairy Production", "Fruit Farming", "Vegetable Farming", "Livestock Production", "Aquaculture", "Crop Production"]
data = [43, 97, 17, 36, 96, 60, 68]
line_labels = ["Category", "Number"]

# setup
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# draw the sectors
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])

# add legend
ax.legend(data_labels, bbox_to_anchor=(1.1, 1.1))

# add labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)

# add title
plt.title("Number of Farms by Type of Food Production in 2021")

# save
fig.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_15.png")

# clear
plt.clf()
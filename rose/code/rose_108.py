
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Urban Areas", "Suburban Areas", "Rural Areas", "Coastal Areas", "Mountain Areas", "Desert Areas"]
data = [1200, 1000, 800, 600, 400, 200]
line_labels = ["Region", "Number of Homes"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Loop to create sectors
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=plt.cm.Set1(i/num_categories), label=data_labels[i])

# Set theta ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=15)

# Set legend
ax.legend(bbox_to_anchor=(1.25, 1), fontsize=15)

# Set title
ax.set_title("Number of Homes in Different Regions in 2021", fontsize=20)

# Save figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-054203_6.png")

# Clear current image
plt.clf()
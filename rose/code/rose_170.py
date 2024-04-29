
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ["Animal Husbandry", "Crop Cultivation", "Food Processing", "Plantation", "Livestock", "Agroforestry", "Fisheries", "Aquaculture"]
data = [50, 70, 90, 60, 90, 80, 30, 20]
line_labels = ["Category", "Number"] 

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection='polar')
ax.set_title("Food Production in Agriculture by Category in 2021")

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, wrap=True, rotation=90)
ax.legend(bbox_to_anchor=(1.1, 1.1), loc="upper left")

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_75.png')
plt.clf()
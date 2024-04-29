
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ["Road","Rail","Air","Water","Pipeline","Other"]
data = [200, 150, 100, 50, 30, 20]
line_labels = ["Mode of Transportation","Number of Commuters"]

fig = plt.figure(figsize=(12, 8)) 
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, bottom=0.0, label=data_labels[i]) 

ax.legend(loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False)) 
ax.set_xticklabels(data_labels, fontsize=12, rotation=45)
ax.set_title("Number of Commuters by Transportation Mode in 2021")
plt.tight_layout() 
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_73.png")
plt.clf()

import matplotlib.pyplot as plt 
import numpy as np

data_labels = ["Mechanical Engineering", "Electrical Engineering", "Computer Science", "Civil Engineering", "Chemical Engineering", "Aerospace Engineering", "Materials Science", "Biomedical Engineering"]
data = [50, 60, 70, 80, 90, 100, 110, 120]
line_labels = ["Field", "Number of Projects"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

colors = [f"C{i}" for i in range(num_categories)]

for i, d in enumerate(data):
    ax.bar(sector_angle * i, d, width=sector_angle, color=colors[i], label=data_labels[i])
    
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True, ha="center")

ax.set_title("Number of Scientific and Engineering Projects in 2021")
ax.legend(bbox_to_anchor=(1.2, 0.5))

fig.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_96.png")
plt.clf()
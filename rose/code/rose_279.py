
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["History","Literature","Psychology","Philosophy","Sociology","Political Science","Economics","Education","Anthropology"]
data = np.array([105,87,90,64,77,105,90,60,50])
line_labels = ["Subject","Number"]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=f"C{i}")

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True)
ax.legend(bbox_to_anchor=(1.2, 0.8))
plt.title("Number of Universities Offering Programs in Social Sciences and Humanities")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_76.png")
plt.clf()
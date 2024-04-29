
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Recruiting", "Onboarding", "Training & Development", "Performance Management", "Compensation & Benefits", "Employee Relations", "Compliance", "Leadership Development"]
data = [27, 56, 84, 54, 41, 32, 23, 14]
line_labels = ["Category", "Number"]

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111, projection='polar')

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, bottom=0.0, label=data_labels[i], color=plt.cm.hsv(i / num_categories))

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.title("Employee Management by Category in 2021")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_140.png")
plt.clf()
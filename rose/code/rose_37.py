
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Disease Prevention', 'Vaccinations', 'Health Education', 'Mental Health', 'Chronic Disease Management', 'Nutrition', 'Physical Activity', 'Injury Prevention', 'Substance Abuse']
data = np.array([90, 87, 80, 70, 60, 50, 40, 30, 20])
line_labels = np.array([i for i in range(0, len(data))])

fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111, projection='polar', facecolor='#d8dcd6')

sector_angle = (2 * np.pi) / len(data)

for i, data_line in enumerate(data):
    ax.bar(x=line_labels[i] * sector_angle, height=data[i], width=sector_angle)

ax.set_xticks(line_labels * sector_angle)
ax.set_xticklabels(data_labels, fontsize=14, wrap=True)
ax.legend(data_labels, fontsize=14, bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_title('Number of Health Programs by Category in 2021', fontsize=20)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_125.png')
plt.cla()
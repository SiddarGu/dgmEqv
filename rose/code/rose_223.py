
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Chemistry', 'Physics', 'Biology', 'Mechanical Engineering', 'Electrical Engineering', 'Aerospace Engineering', 'Civil Engineering', 'Computer Science', 'Biomedical Engineering']
data = [180, 150, 100, 130, 110, 90, 70, 50, 30]
line_labels = ['Discipline', 'Number of Researchers']

# Plot the data
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

colors = ["#00b8ff", "#00e5ff", "#00ffc5", "#a8ff00", "#ffaa00", "#ff4d00", "#ff00aa", "#b800ff", "#7500ff"]
sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels)))
ax.set_xticklabels(data_labels, fontsize=8, rotation=45, ha='right')
ax.legend(bbox_to_anchor=(1.3, 1), frameon=False)
ax.set_title('Number of Researchers in Various Disciplines of Science and Engineering')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_42.png')
plt.clf()
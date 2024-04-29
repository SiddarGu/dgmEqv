
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Web Design', 'Software Development', 'Cyber Security', 'Data Science', 'Networking', 'Mobile Development', 'Artificial Intelligence']
data = [25, 40, 60, 30, 15, 20, 50]
line_labels = ['Number']

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='polar')
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

sector_angle = (2 * np.pi) / len(data_labels)
colors = ['b','r','c','m','y','k','g']

for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=colors[i])

ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels)

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.title('Number of Tech Professionals Specializing in Each Field')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_46.png')

plt.clf()
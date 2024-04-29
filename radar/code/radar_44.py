
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Appeal (Score)', 'Popularity (Rating)', 'Quality (Score)', 'Engagement (Score)', 'Accessibility (Score)']
data = [[92, 95, 110, 105], [8, 9, 10, 11], [85, 90, 95, 100], [90, 95, 100, 105], [80, 85, 90, 95]]

plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)
angles = np.linspace(0, 2*np.pi, len(data_labels)+1, endpoint=True)
ax.set_thetagrids(angles[:-1]*180/np.pi, data_labels, fontsize=14)
ax.set_rlim(0, max(map(max, data))+10)
ax.grid(True)

for line_data, line_label in zip(data, line_labels):
    line_data = np.append(line_data, line_data[0])
    ax.plot(angles, line_data, label=line_label)

ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.05))
plt.title('Sports and Entertainment Performance Evaluation', fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/radar/png_val/radar_44.png')
plt.clf()
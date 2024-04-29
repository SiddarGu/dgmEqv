

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Primary Care', 'Mental Health Care', 'Urgent Care', 'Emergency Care', 'Rehabilitation Care', 'Hospice Care', 'Palliative Care', 'Surgical Care']
data = [60, 50, 45, 40, 35, 30, 25, 20]
line_labels = ['Type of Care', 'Number of Patients']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

angles = np.arange(0, 2*np.pi, sector_angle)

for i in range(num_categories):
    ax.bar(angles[i], data[i], width=sector_angle, label=data_labels[i], edgecolor='black', zorder=3, color=f'C{i}')

ax.set_thetagrids(angles * 180/np.pi, data_labels, fontsize=12, color='grey')
ax.set_title('Number of Patients Receiving Different Types of Care in 2021', fontsize=14)
ax.grid(zorder=0, color='grey', linestyle='-', linewidth=1)
ax.legend(bbox_to_anchor=(0.9, 0.9), fontsize=12)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_77.png')
plt.clf()
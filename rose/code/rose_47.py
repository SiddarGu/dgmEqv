

import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Hospitals', 'Clinics', 'Urgent Care Centers', 'Health Care Facilities', 'Nursing Homes', 'Home Health Care Providers', 'Mental Health Care Providers', 'Mobile Health Services']
data = [540, 360, 240, 180, 140, 120, 60, 40]
line_labels = ['Category', 'Number']

# Plot data
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

colors = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=16, wrap=True, rotation=sector_angle/2)

ax.legend(bbox_to_anchor=(1.2, 1.0), fontsize=16)
ax.set_title('Number of Health Care Providers in The United States', fontsize=20)

plt.tight_layout()
plt.savefig(
    '/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_14.png')
plt.clf()
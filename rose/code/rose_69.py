
import matplotlib.pyplot as plt
import numpy as np

# Transformation of raw data
data_labels = ['Recruiting','Training and Development','Performance Management','Employee Relations','Compensation and Benefits','Occupational Safety and Health']
data = [60,50,40,30,20,10]
line_labels = ['Category','Number']

# Plotting of rose chart
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, wrap=True, rotation=-90)
ax.legend(bbox_to_anchor=(0.5, 0.2))
ax.set_title('Number of Employees Involved in HR Management in 2021', fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_37.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Recruitment', 'Employee Relations', 'Performance Management', 'Training and Development', 'Compensation and Benefits', 'Diversity and Inclusion', 'Time and Attendance', 'Safety and Health', 'Employee Retention']
data = [500, 360, 250, 200, 150, 120, 90, 60, 30]
line_labels = ['Category', 'Number of Employees']

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'black']
for i, category in enumerate(data_labels):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=category, color=colors[i])
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.legend(bbox_to_anchor=(1, 1), loc="upper right", bbox_transform=fig.transFigure)
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)
ax.set_title('Number of Employees in Human Resources and Employee Management in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_24.png')
plt.clf()
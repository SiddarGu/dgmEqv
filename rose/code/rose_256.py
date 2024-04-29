
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Recruiting', 'Training', 'Payroll', 'Performance Management', 'Benefits', 'Staff Development', 'HR Policies', 'Employee Relations', 'Organizational Development']
data = [88, 90, 78, 84, 82, 76, 92, 70, 94]
line_labels = ['Category', 'Number']

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=18, wrap=True, rotation=45)
ax.legend(bbox_to_anchor=(1,1.05), fontsize=15)
ax.set_title('Quantifying HR & Employee Management Practices in 2021', fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_3.png')
plt.clf()
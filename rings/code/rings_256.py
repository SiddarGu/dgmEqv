
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Training and Development', 'Performance Appraisal', 'Job Satisfaction', 'Recruitment', 'Employee Benefits']
data = np.array([31, 23, 19, 17, 10])
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['b', 'g', 'r', 'c', 'm'])
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='upper right')
ax.set_title('HR Management and Employee Engagement - 2023')
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_109.png')
plt.clf()
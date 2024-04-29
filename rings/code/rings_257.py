
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Employee Retention', 'Training Efficiency', 'Workforce Development', 'Productivity', 'Job Satisfaction']
data = np.array([34, 12, 30, 22, 2])
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['b', 'g', 'r', 'c', 'm'])
circle = plt.Circle((0, 0), radius=0.7, fc='white')
ax.add_artist(circle)
ax.set_title('Human Resources and Employee Management Performance - 2023')
ax.legend(data_labels, loc='best')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_112.png')
plt.clf()
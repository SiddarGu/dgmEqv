
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Employee Training', 'Employee Retention', 'Employee Performance', 'Diversity & Inclusion', 'Workplace Satisfaction']
data = [20, 21, 29, 10, 20]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['darkorange', 'cornflowerblue', 'limegreen', 'lightcoral', 'mediumslateblue'])
circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc="upper right")

plt.title("Human Resources and Employee Management Report - 2023", fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_7.png')
plt.clf()
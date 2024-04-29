
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_labels = ['Recruitment', 'Training', 'Retention', 'Performance', 'Employee Engagement']
data = [19, 18, 25, 19, 19]
line_labels = [1, 2, 3, 4, 5]

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(1, 1, 1)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False,autopct='%1.1f%%',labeldistance=1.05)
ax.add_artist(plt.Circle((0,0), radius = 0.7, fc = 'white'))
ax.set_title('Employee Management Analysis - 2023')
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.8))
plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_119.png')
plt.clf()
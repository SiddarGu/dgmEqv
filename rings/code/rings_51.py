
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Staff Retention', 'Recruitment', 'Training', 'Career Progression', 'Workplace Safety']
data = [25, 20, 25, 15, 15]
line_labels = ['Category', 'Ratio']

fig, ax = plt.subplots(figsize=(10,7))
ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%')
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.set_title("Employee Management - 2021")
ax.legend(data_labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_112.png')
plt.close()
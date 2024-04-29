
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Productivity','Retention','Training Effectiveness','Recruitment','Diversity']
data = [41,21,16,12,10]
line_labels = ['Category']

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['red','green','blue','yellow','orange'])
inner_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(inner_circle)
ax.legend(data_labels, loc='best',frameon=False)
plt.title('HR & Employee Management Report - 2023', fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_103.png')
plt.clf()
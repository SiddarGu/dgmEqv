
import matplotlib.pyplot as plt
import numpy as np

data_labels=['Production Efficiency','Quality Control','Employee Welfare','Cost Management','Customer Satisfaction']
data=[23,15,7,30,25]
line_labels=['Category','ratio']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

ax.pie(data,labels=data_labels,startangle=90,counterclock=False,textprops={'fontsize': 10})
circle=plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)

ax.set_title('Food and Beverage Industry Performance - 2023')
ax.legend(data_labels, loc='best', bbox_to_anchor=(1, 1), fontsize=10)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_105.png')
plt.clf()
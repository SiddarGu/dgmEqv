
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Recruitment','Retention','Employee Satisfaction',
               'Training & Development','Performance Management']
data = np.array([18,15,25,25,17])
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot()

ax.pie(data, colors=['red', 'darkorange', 'gold', 'c', 'dodgerblue'],
       startangle=90, counterclock=False,
       wedgeprops={'linewidth': 2, 'edgecolor': 'black'},
       textprops={'fontsize': 11})

inner_circle = plt.Circle((0,0), 0.4, color='white', fc='white', linewidth=0)
ax.add_artist(inner_circle)

ax.legend(data_labels, loc='best', fontsize=14)
ax.set_title('Human Resources Management - 2023', fontsize=18)

plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_67.png')
plt.clf()
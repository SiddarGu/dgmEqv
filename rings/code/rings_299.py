
import matplotlib.pyplot as plt
import numpy as np
 
data_labels = ['Recruitment','Training','Performance Evaluation','Salary & Benefits','Retention']
data = np.array([20,15,15,35,15])
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False)
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels)
plt.title('Human Resources Efficiency - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_34.png')
plt.clf()
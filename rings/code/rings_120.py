
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Delivery Time', 'Transport Availability', 'Cost Efficiency', 'Quality of Service', 'Safety Standards'] 
line_labels = ['Category']
data = np.array([20, 15, 35, 20, 10])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
explode = (0.1, 0, 0, 0, 0)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, explode=explode, autopct='%.0f%%')
centre_circle = plt.Circle((0,0),0.7,fc='white', linewidth=0)
ax.add_artist(centre_circle)
ax.axis('equal')
ax.set_title('Transportation and Logistics Efficiency - 2023')
ax.legend(data_labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
plt.savefig(r'/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_71.png')
plt.clf()
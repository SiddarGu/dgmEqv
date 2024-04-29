
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ['Delivery Time','Route Efficiency','Vehicle Maintenance','Fuel Consumption','Safety']
line_labels = ['Category']
data = np.array([[25,15,27,19,14]])

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
ax.pie(data.reshape(-1), labels=data_labels, colors=['red','orange','yellow','green','blue'], startangle=90, counterclock=False)
center_circle = plt.Circle((0,0),0.7,fc='white')
ax.add_artist(center_circle)
ax.axis('equal')
ax.set_title('Transportation & Logistics Performance - 2023')
ax.legend(data_labels, loc=4)
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_135.png')
plt.clf()
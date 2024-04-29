
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Labor Costs', 'Materials Costs','Equipment Costs', 'Shipping Costs', 'Overhead Costs'] 
data = np.array([22, 27, 13, 20, 18]) 
line_labels = ['Category']

fig = plt.figure(figsize=(12,8)) 
ax = fig.add_subplot(111) 
ax.pie(data, labels=data_labels, autopct='%1.1f%%')
ax.set_title('Manufacturing and Production Expenditure - 2023')

centre_circle = plt.Circle((0,0),0.5,color='white')
ax.add_artist(centre_circle)
ax.axis('equal') 
ax.legend(data_labels, loc='upper right') 
plt.tight_layout() 

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_39.png') 
plt.clf()
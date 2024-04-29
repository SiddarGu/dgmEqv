
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Sponsorship','Attendance','Merchandise','Broadcast','Media Exposure'] 
data = np.array([17,20,24,22,17]) 
line_labels = ['Category'] 

fig = plt.figure(figsize=(8,8)) 
ax = fig.add_subplot(111) 
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors = ['blue','orange','green','red','purple']) 
centre_circle = plt.Circle((0,0), 0.6, color='white', fc='white',linewidth=0) 
ax.add_artist(centre_circle) 
ax.set_title('Sports and Entertainment Industry Performance - 2023') 
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.7)) 
plt.tight_layout() 
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_23.png') 
plt.clf()
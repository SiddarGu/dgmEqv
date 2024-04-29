
import matplotlib.pyplot as plt 
import numpy as np 
data_labels=["Renewable Energy","Fossil Fuels","Nuclear Power","Hydroelectricity"] 
data=np.array([44,25,14,17]) 
line_labels=["Type","ratio"]

fig = plt.figure(figsize=(10,10)) 
ax = fig.add_subplot(111) 
ax.pie(data,labels=data_labels,autopct='%1.1f%%',startangle=90,counterclock=False,colors=['blue','brown','yellow','green']) 
center_circle = plt.Circle((0,0),0.7,fc='white') 
fig = plt.gcf() 
ax.add_artist(center_circle) 
ax.axis('equal') 
plt.title("Energy Resources Utilization - 2023") 
ax.legend(data_labels, loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.2)) 
plt.tight_layout() 
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_20.png') 
plt.clf()
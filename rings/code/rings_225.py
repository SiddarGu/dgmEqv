
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ["Criminal","Civil","Corporate","Regulatory","Tax"]
data = np.array([32,17,13,20,18])
line_labels = ["Area","ratio"]

fig = plt.figure(figsize=(8,8)) 
ax = fig.add_subplot(111)
plt.title("Law and Legal Affairs Overview - 2023")
ax.pie(data, labels=data_labels, startangle=90,counterclock=False,autopct='%1.1f%%') 
centre_circle = plt.Circle((0,0),0.5,fc='white')
fig = plt.gcf() 
ax.add_artist(centre_circle) 
plt.legend(data_labels, loc="lower right",bbox_to_anchor=(1.1,0.5)) 
plt.tight_layout()
plt.savefig(r"/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_87.png")
plt.cla()
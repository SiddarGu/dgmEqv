
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Network Security','Software Development','Infrastructure','Artificial Intelligence','E-commerce']
data = [20,15,17,14,34]
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()
ax.pie(data,startangle=90,counterclock=False,labels=data_labels,colors=['b','g','r','y','c'])
centre_circle = plt.Circle((0,0),0.5,color='white')
ax.add_artist(centre_circle)
ax.set_title('Technology and Internet Trends - 2023')
ax.legend(data_labels, loc="lower right")
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_20.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

data_labels=['Network Security','Data Storage','Online Presence','Infrastructure','User Interface']
data=[0.15,0.1,0.25,0.3,0.2]
line_labels=['Category','ratio']

fig,ax=plt.subplots(figsize=(6,6))
ax.axis('equal')
ax.pie(data,labels=data_labels,startangle=90,counterclock=False)
plt.Circle(xy=(0,0),radius=0.5,color='white')
ax.add_artist(plt.Circle(xy=(0,0),radius=0.5,color='white'))
ax.legend(data_labels,loc='best')
plt.title('Technology and the Internet - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_115.png')
plt.clf()
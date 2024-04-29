
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Policy Implementation','Legislation','Citizen Satisfaction','Tax Revenue','Fiscal Management']
line_labels = ['Category']
data = np.array([[17,22,25, 16, 20]])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.pie(data[0],startangle=90,counterclock=False,labels=data_labels,autopct='%1.1f%%',colors=['b','m','c','r','g'])

circle = plt.Circle((0,0),.7,color='white')
ax.add_artist(circle)
ax.legend(data_labels,bbox_to_anchor=(1,0.5), loc="center right")
plt.title('Government Performance - 2023',size=15)
plt.tight_layout()

plt.savefig(r'/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_149.png')
plt.close()

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Education','Culture','Geography','History','Psychology']
data = np.array([25,15,35,15,10])
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(data,labels=data_labels, colors=['#FDB813', '#FFD43B', '#FFF200', '#9ACD32', '#006400'], startangle=90, counterclock=False, wedgeprops={'width': 0.5, 'edgecolor': 'white'})
centre_circle = plt.Circle((0,0), 0.8, color='white', fc='white',linewidth=1.25)
ax.add_artist(centre_circle)
ax.set_title('Social Sciences and Humanities Study Overview - 2021', fontsize=20)
ax.legend(data_labels,fontsize=14, loc='upper left', bbox_to_anchor=(-0.1,1))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_95.png')
plt.close()
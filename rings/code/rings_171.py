
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Visitor Satisfaction','Tourist Attractions','Service Quality','Location Appeal','Accessibility']
line_labels = ['Category','ratio']
data = np.array([['Visitor Satisfaction',35],['Tourist Attractions',25],['Service Quality',15],['Location Appeal',20],['Accessibility',5]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data[:,1], labels=data[:,0], startangle=90,counterclock=False,colors=['#5cbae6','#b6d957','#fac364','#8cd3ff','#d998cb'])

circle = plt.Circle(xy=(0,0), radius=0.7, facecolor='white',edgecolor='white')
ax.add_artist(circle)

ax.legend(data_labels, loc='upper right',bbox_to_anchor=(-0.1, 1))
ax.set_title('Tourism and Hospitality Industry Overview - 2023',fontsize=20)
ax.grid(True)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_145.png')
plt.cla()
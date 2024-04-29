
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

data_labels = ['Student Performance', 'Academic Rigor', 'School Resources', 'Teacher Quality', 'Parental Involvement']
line_labels = ['Category']
data = np.array([['Category', 'ratio'], ['Student Performance', 37], ['Academic Rigor', 25], ['School Resources', 15], ['Teacher Quality', 18], ['Parental Involvement', 5]])

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)

colors = cm.rainbow(np.linspace(0, 1, len(data_labels)))
wedges, texts = ax.pie(data[1:, 1], startangle=90, counterclock=False, colors=colors, wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})

centre_circle = plt.Circle((0,0),0.50,color='white', fc='white',linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.axis('equal')
ax.legend(labels=data_labels, loc="lower right", bbox_to_anchor=(1, 0), fontsize=15, bbox_transform=ax.transAxes)
ax.set_title('Education Quality Measurement - 2023', fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_99.png')
plt.clf()
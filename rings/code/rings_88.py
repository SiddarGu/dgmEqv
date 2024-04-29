
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['User Engagement', 'Data Analytics', 'Traffic Sources', 'Advertising', 'Web Design']
line_labels = ['Category', 'ratio']
data = np.array([[32, 15, 7, 26, 20]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

cmap = plt.cm.tab20(np.arange(len(data_labels)))
ax.pie(data[0], labels=data_labels, colors=cmap, startangle=90, counterclock=False)

ax.set_title('Social Media and Web Performance Overview - 2023')

circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

ax.legend(data_labels, bbox_to_anchor=(1,0.5), loc="center left", bbox_transform=ax.transAxes, fontsize='medium',ncol=1, frameon=False)

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_29.png')
plt.clf()
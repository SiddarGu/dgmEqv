
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ['Ticket Sales', 'Sponsorship', 'Merchandise', 'Media Rights', 'Event Participation']
line_labels = ['Category', 'ratio']
data = np.array([['Ticket Sales', 35], ['Sponsorship', 25], ['Merchandise', 20], ['Media Rights', 15], ['Event Participation', 5]])

fig = plt.figure(figsize=(11,11))
ax = fig.add_subplot(111)

ax.pie(data[:,1], labels=data[:,0], startangle=90, counterclock=False, colors=['red','green','blue','orange','pink'])

inner_circle = mpatches.Circle((0, 0), 0.70, fc='white')
ax.add_artist(inner_circle)

ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1))

ax.set_title('Sports and Entertainment Revenue - 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_24.png')
plt.clf()
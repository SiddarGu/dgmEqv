
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Online Sales', 'Offline Sales', 'Delivery Efficiency', 'Customer Service', 'Product Quality']
data = [41, 24, 15, 12, 8]
line_labels = []

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()

colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF']
ax.pie(data, labels=data_labels, colors=colors, startangle=90, counterclock=False)
pie_wedge_collection = ax.pie(data, labels=data_labels, colors=colors, startangle=90, counterclock=False)

centre_circle = plt.Circle((0,0),0.5,color='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.legend(data_labels)
ax.set_title('E-commerce and Retail Performance - 2023')
ax.grid(True)
ax.axis('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_109.png')
plt.clf()
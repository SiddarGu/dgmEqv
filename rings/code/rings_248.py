
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Tourism Revenue', 'Hospitality Quality', 'Customer Satisfaction', 'Tourism Impact', 'Cultural Preservation']
data = np.array([33, 35, 19, 7, 6])
line_labels = ['Category']

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
center_circle = plt.Circle((0,0),0.7,color='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)
ax.legend(data_labels, loc='upper right')
ax.set_title('Tourism and Hospitality Trends - 2023', fontsize=16)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_8.png')
plt.clf()

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

data_labels = ['Media Exposure', 'Fans Enthusiasm', 'Sponsorship Deals', 'Player Performance', 'Brand Image']
data = np.array([20, 30, 15, 25, 10])
line_labels = ['Category']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

centre_circle = Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
ax.add_artist(centre_circle)

ax.legend(data_labels, loc="lower left")
ax.set_title('Sports and Entertainment Analysis - 2023')

fig.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_18.png')

plt.clf()
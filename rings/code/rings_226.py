
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Website Traffic', 'Social Engagement', 'User Satisfaction', 'Digital Advertising']
data = [25, 36, 15, 24]
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
radii = data
colors = plt.cm.Paired(np.arange(len(data)))
ax.pie(radii, labels=data_labels, colors=colors, startangle=90, counterclock=False)
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.8))
plt.title('Social Media and the Web Performance Metrics - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_88.png')
plt.clf()
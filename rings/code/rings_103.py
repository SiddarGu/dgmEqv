
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Website Traffic', 'Social Media Engagement', 'Online Advertising', 'Content Quality', 'User Experience']
data = np.array([30, 25, 20, 12, 13])
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%.1f%%', labeldistance=0.8)
ax.axis('equal')
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.set_title('Social Media and Web Performance - 2023')
ax.legend(data_labels, bbox_to_anchor=(1, 0.8), loc='best', fontsize=10, bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_51.png')
plt.clf()
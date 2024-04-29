
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ['Fundraising', 'Philanthropic Activities', 'Social Programs', 'Outreach Activities', 'Donor Relations']
data = [24, 14, 33, 14, 15]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=plt.cm.Set1(np.arange(len(data))))
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.axis('equal')
ax.legend(data_labels)
ax.set_title('Impact of Nonprofits - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_77.png')
plt.clf()
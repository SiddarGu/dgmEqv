
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Online Shopping','In-Store Shopping','Delivery Services','Returns']
data = np.array([0.33, 0.41, 0.19, 0.07])
line_labels = ['Category','Ratio']

fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(111)
ax.pie(data, startangle = 90, counterclock = False, colors = ['blue','yellow','green','orange'], labeldistance = 0.9, autopct='%1.1f%%')
inner_circle = plt.Circle((0, 0), 0.3, color = 'white')
ax.add_artist(inner_circle)
ax.legend(data_labels, loc = 'upper left', bbox_to_anchor = (0.8, 0.9))
plt.title('Retail and E-commerce Trends - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_116.png')
plt.clf()
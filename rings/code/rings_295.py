
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig = plt.figure(figsize=(13,7))
data_labels = ['Online Orders', 'Store Visits', 'Return Customers', 'New Customers', 'Delivery Time']
data = [42, 17, 16, 23, 2]
line_labels = ['Category', 'ratio']
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, autopct='%.2f%%', textprops={'fontsize': 12}, startangle=90, counterclock=False, colors=['coral', 'royalblue', 'yellowgreen', 'dodgerblue', 'orchid'])
ax.axis('equal')
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.set_title('Impact of E-commerce on Retail Sales - 2021', fontsize=14)
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.35,1.0), fontsize=12)
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_3.png')
plt.clf()
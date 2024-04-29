
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Energy','Fossil Fuels','Hydroelectricity','Nuclear Power','Other Sources']
data = [36,27,15,16,6]
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False,autopct='%1.2f%%')
circle = plt.Circle(xy=(0, 0), radius=0.6, fc='white')
ax.add_artist(circle)
ax.set_title('Energy Usage Status - 2023')
ax.legend(data_labels,bbox_to_anchor=(1.1, 0.5))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_46.png')
plt.clf()
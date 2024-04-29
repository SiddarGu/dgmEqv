
import matplotlib.pyplot as plt
import numpy as np
import os

data_labels=['Renewable Energy Usage','Waste Management','Air Quality','Water Quality','Carbon Emission']
data=[50,15,15,15,5]
line_labels=['Category']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()
ax.pie(data, colors=['#b2df8a', '#33a02c', '#a6cee3', '#1f78b4', '#e31a1c'], 
       startangle=90, counterclock=False, autopct='%1.1f%%')
ax.set_title('Environmental Sustainability Measurement in 2023', fontsize=16)

circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

ax.legend(data_labels, bbox_to_anchor=(1.0, 1.0))
ax.axis('equal')
plt.tight_layout()
plt.savefig(os.path.join('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_9.png'))
plt.clf()
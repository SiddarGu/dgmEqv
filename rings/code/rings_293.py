
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

data_labels = ['Logistics Efficiency', 'Delivery Reliability', 'Transportation Cost', 'Safety Record', 'Maintenance']
data = [41, 20, 27, 7, 5]
line_labels = ['Category']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#00FF00', '#FF00FF', '#FF9900', '#99CCFF', '#FFFF00'])

circle = Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.set_title("Transportation and Logistics Performance Evaluation - 2023")
ax.legend(data_labels, loc='best')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_24.png', bbox_inches='tight')
plt.clf()

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ['Customer Acquisition', 'Sales Volume', 'Customer Retention', 'Return on Investment', 'Advertising Efficiency']
line_labels = ['Category', 'ratio']
data = [[14,19,22,17,28]]

fig, ax = plt.subplots(figsize=(10,8))
explode = (0, 0, 0, 0, 0.1)
ax.pie(data[0], labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False, explode=explode)
circle = mpatches.Circle((0, 0), 0.75, fc='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.title('Retail and E-commerce - Performance Overview - 2023', fontsize='large', fontweight='bold', wrap=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_142.png')
plt.clf()
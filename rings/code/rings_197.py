
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Production Costs', 'Distribution Costs', 'Advertising', 'Overhead', 'Profit']
data = [36, 17, 18, 14, 15]
line_labels = ['Category', 'ratio']

fig, ax = plt.subplots(figsize=(12, 8))
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False)
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.title.set_text('Food and Beverage Industry Performance - 2023')
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=5, fontsize=14)
ax.axis('equal') 
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_47.png')
plt.clf()
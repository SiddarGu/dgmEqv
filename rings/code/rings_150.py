
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Tax Revenue', 'Education', 'Social Welfare', 'Infrastructure', 'Security']
data = [10, 20, 39, 25, 6]
line_labels = ['Category', 'Ratio']

fig, ax = plt.subplots(figsize=(14, 8))
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%1.1f%%')
centre_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(centre_circle)
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.2, 0.8))
ax.set_title('Government Performance - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_115.png')
plt.clf()
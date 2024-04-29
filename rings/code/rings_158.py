
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ['Law Enforcement', 'Court Cases', 'Legal Services', 'Regulatory Compliance', 'Education']
data = [14,37,11,25,13]
line_labels = np.arange(len(data))

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Legal Affairs Overview - 2023')
pie = ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False, textprops={'fontsize': 12})
circle = plt.Circle((0, 0), 0.6, color='white', fc='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.2, 1))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_124.png')
plt.clf()
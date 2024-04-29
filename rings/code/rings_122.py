
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ["Research & Development", "Productivity", "Quality", "Efficiency", "Safety"]
data = [30, 18, 15, 22, 15]
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

inner_circle = plt.Circle((0, 0), 0.6, color='white', fc='white', linewidth=1.25)

ax.add_artist(inner_circle)
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1))
ax.set_title('Science and Engineering Performance - 2023')
ax.axis('equal')

plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='both', which='both')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_74.png', bbox_inches='tight')
plt.clf()
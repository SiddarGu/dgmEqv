
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ["Profit Margin", "Expenses", "Investments", "Revenue", "Market Share"]
line_labels = ["Category", "ratio"]
data = [[26,50,7,15,2]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
ax.pie(data[0], labels=data_labels, autopct='%1.1f%%', colors=colors, startangle=90, counterclock=False)
inner_circle = plt.Circle((0, 0), 0.70, color='white')
ax.add_artist(inner_circle)
ax.set_title('Financial Performance Evaluation - 2023')
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.5), loc="center right")
ax.grid(True, linestyle='-.')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_136.png')
plt.clf()
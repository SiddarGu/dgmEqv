
import matplotlib.pyplot as plt
import numpy as np

data_labels = np.array(['Profit', 'Expenses', 'Investments', 'Revenue', 'Market Share'])
data = np.array([33, 25, 14, 17, 11])
line_labels = np.array(['Category'])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['#ff0000','#00ff00','#0000ff','#ffff00','#ff00ff'])

inner_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(inner_circle)
ax.legend(data_labels, bbox_to_anchor=(1, 0.5))

ax.set_title('Business Profitability and Performance - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_41.png')
plt.clf()
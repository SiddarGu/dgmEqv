
import matplotlib.pyplot as plt 
import matplotlib as mpl
import numpy as np

data_labels = np.array(['Profit', 'Expenses', 'Investments', 'Revenue', 'Market Share'])
data = np.array([24, 30, 15, 25, 6])
line_labels = np.array(['Category'])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
explode = (0, 0, 0, 0, 0)
cmap = mpl.cm.RdYlGn
ax.pie(data, explode=explode, labels=data_labels, colors=cmap(data / data.max()), autopct='%1.1f%%',
        shadow=True, startangle=45, counterclock=False)

centre_circle = plt.Circle((0, 0), 0.5, color='white', fc='white', linewidth=1.25)
ax.add_artist(centre_circle)
ax.grid(True, color='black', linestyle='-.', linewidth=1, alpha=0.7)
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
plt.title('Financial Performance in Business - 2023', fontsize=15, fontname='sans-serif', pad=20)
ax.axis('equal')
fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_143.png')
plt.clf()
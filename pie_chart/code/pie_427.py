
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)

labels = ['Equity','Bonds','Mutual funds','ETFs','Cash']
sizes = [30,30,20,10,10]
colors = ['red','orange','yellow','green','blue']

ax.pie(sizes, colors=colors, labels=labels, autopct='%1.f%%',pctdistance=0.85, labeldistance=1.05,
        rotatelabels=True, textprops={'fontsize': 11, 'color':'black'})

ax.legend(labels,
          title="Investment Type",
          bbox_to_anchor=(1, 0.5),
          loc="center right",
          fontsize=11,
          framealpha=1)

plt.title('Investment Portfolio Allocation in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/162.png')
plt.clf()
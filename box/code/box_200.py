
import matplotlib.pyplot as plt
import numpy as np

charity_data = {
    'Charity A': [50, 100, 150, 250, 350],
    'Charity B': [80, 140, 200, 280, 400, 450],
    'Charity C': [75, 125, 175, 275, 375, 500, 550],
    'Charity D': [60, 110, 160, 210, 310, 400, 450],
    'Charity E': [70, 120, 170, 220, 320, 350]
}

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title('Donation Distribution in Charitable Organizations (2021)')
ax.set_xlabel('Home Type')
ax.set_ylabel('Donation (USD)')
ax.grid(True, ls='--')

# plot boxplot
data = list(charity_data.values())
outliers = [data[i][5:] if len(data[i]) > 5 else [] for i in range(len(data))]
bp = ax.boxplot(np.array([data[i][:5] for i in range(5)]).T, widths=0.6)
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i+1] * len(outlier), outlier, 'ro', alpha=0.6)
# add x-axis labels
ax.set_xticklabels(list(charity_data.keys()), rotation=45, ha='right', wrap=True)

# plot outliers
for i, l in enumerate(bp['fliers']):
    if l.get_ydata():
        x = np.ones_like(l.get_ydata()) * i
        ax.plot(x, l.get_ydata(), 'ro', alpha=0.7)

# figure layout
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/15_202312251044.png')

# clear current figure
plt.clf()
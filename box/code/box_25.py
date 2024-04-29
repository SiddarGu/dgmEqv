
import matplotlib.pyplot as plt
import numpy as np

data = [[200,400,600,800,1000],
        [300,500,700,900,1200],[400,600,800,1000,1200],
        [500,700,900,1100,1300],[400,500,700,900,1100]]
outliers = [[],[1500],[50,1300],[1400],[1250,1300]]
line_labels = ['Education', 'Healthcare', 'Housing', 'Scoidal Welfare', 'Transportation']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

ax.set_title("Program Cost Distribution in US Government in 2021")
ax.set_xticklabels(line_labels)
ax.set_ylabel("Cost (USD)")
ax.boxplot(data, whis=1.5)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, "o")

ax.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/29_202312251608.png")
plt.clf()
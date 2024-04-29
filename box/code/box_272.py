
import matplotlib.pyplot as plt
import numpy as np

# restructured data
data = [[1000, 3000, 5000, 7000, 14000], 
        [4000, 6000, 8000, 10000, 18000], 
        [10000, 20000, 30000, 40000, 60000], 
        [20000, 40000, 60000, 80000, 100000], 
        [50000, 70000, 90000, 110000, 140000]]
outliers = [[], [20000], [50000, 80000], [], []]
line_labels = ['Small Loans', 'Medium Loans', 'Large Loans', 'Jumbo Loans', 'Super Jumbo Loans']

# plot boxplot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_title('Loan Size Distribution of Business and Finance in 2021')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Loan Size (USD)')
ax.boxplot(data, whis=1.5)

# plot outliers
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        x = [i + 1] * len(outlier)
        ax.plot(x, outlier, 'o', color='blue', markersize=4)

# draw grids
ax.yaxis.grid(True)

# save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/50_202312270030.png')

# clear fig
plt.clf()
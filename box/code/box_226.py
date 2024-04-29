import matplotlib.pyplot as plt
import numpy as np

data = [
    ["Entry Level", 35000, 42000, 46000, 53000, 60000, []],
    ["Mid Level", 60000, 68000, 74000, 80000, 90000, [50000, 100000]],
    ["Senior Level", 90000, 98000, 105000, 114000, 120000, [80000, 130000]],
    ["Managers", 120000, 135000, 148000, 160000, 175000, [100000, 190000]],
    ["Executive", 175000, 200000, 225000, 250000, 300000, [160000, 320000]]
]

# Restructuring data
categories, data_2d, outliers_2d = [], [], []
for row in data:
    categories.append(row[0])
    data_2d.append(row[1:6])
    outliers_2d.append(row[6])

# Create figure
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)

# Box plotting
bp = ax1.boxplot(data_2d, sym='', widths=0.6, vert=True, whis=1.5)

# Plotting outliers manually
for i, outlier in enumerate(outliers_2d):
    if outlier:
        ax1.plot([i + 1] * len(outlier), outlier, 'x', color='red')

# Customizing plot
plt.setp(bp['medians'], color='blue')
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax1.set_axisbelow(True)
ax1.set_title('Salary Distribution by Employee Levels in 2022')
ax1.set_xlabel('Employee Level')
ax1.set_ylabel('Salary ($)')
plt.xticks(np.arange(1,len(categories)+1), categories, rotation=45, ha='right')

# Save and clear figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/98_202312270030.png')
plt.clf()

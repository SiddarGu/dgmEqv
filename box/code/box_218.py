import matplotlib.pyplot as plt

# data
data = [
    [1050, 1750, 2050, 2350, 2750],    # Company A
    [1200, 1800, 2100, 2400, 2800],    # Company B
    [1100, 1600, 2000, 2300, 2600],    # Company C
    [950, 1550, 1950, 2250, 2650],     # Company D
    [1000, 1400, 1800, 2200, 2600]     # Company E
]
outliers = [
    [],                 # Company A
    [3000, 5000],       # Company B
    [4000, 4500],       # Company C
    [1050, 1200],       # Company D
    [4000]              # Company E
]
labels = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']

# figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# plot boxplot & markers for outliers 
for i, outlier in enumerate(outliers):
    ax.boxplot(data, notch=True, vert=True, patch_artist=True, labels=labels)
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# title
ax.set_title('Energy Consumption Distribution in Utility Companies (2022)')

# labels
ax.set_xlabel('Utility Companies')
ax.set_ylabel('Energy Consumption (kWh)')

# grid & settings
ax.grid(True)
ax.yaxis.grid(which='major', linestyle='-', linewidth='0.5')
ax.xaxis.grid(True, which='major')
ax.margins(y=0.05)
plt.xticks(rotation=90)

# save image & show it
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/173_202312310058.png', dpi=300)

# clear current plot after saving it
plt.clf()

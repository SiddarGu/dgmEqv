import matplotlib.pyplot as plt

law_firms = ['Adams & Reese',
             'Baker & McKenzie',
             'DLA Piper',
             'Ogletree Deakins',
             'White & Case']

data = [[1, 3, 7, 12, 18], 
        [2, 5, 8, 14, 20],
        [3, 7, 10, 15, 22],
        [2, 4, 9, 13, 19],
        [1, 3, 6, 11, 16]]

outliers_data = [[], 
                 [22, 25],
                 [],
                 [25, 30],
                 [18, 21]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

bp = ax.boxplot(data, whis=1.5)

for i, outlier in enumerate(outliers_data):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(x, outlier, 'ro', alpha=0.6)

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)
ax.set_title('Case Length Analysis across Law Firms in 2022')
ax.set_xlabel('Law Firm')
ax.set_ylabel('Case Length (Months)')
plt.setp(bp['medians'], color='blue')
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

ax.set_xticklabels(law_firms, rotation=30, ha='right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/155_202312310058.png')
plt.clf()

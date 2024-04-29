import matplotlib.pyplot as plt

data='''Company Sector,Min Sales (Million),Q1 Sales (Million),Median Sales (Million),Q3 Sales (Million),Max Sales (Million),Outlier Sales (Million)
Retail,10,25,40,60,90,[100,200]
Manufacturing,15,30,50,80,120,[]
Technology,20,40,70,90,130,[150,220]
Healthcare,30,50,80,110,150,[180,210]
Energy,40,80,120,160,200,[225,230]'''

data = data.split('\n')
sector_data, outliers = [], []

for row in data[1:]:
    items = row.split(',')
    sector_data.append(list(map(int, items[1:6])))
    outliers.append(list(map(int, items[6][1:-1].split())) if items[6][1:-1] else [])

sectors = [row.split(',')[0] for row in data[1:]]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

ax.boxplot(sector_data, notch=True, vert=False, patch_artist=True, whis=1.5)
ax.set_yticklabels(sectors, fontsize=8)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), linestyle='None', marker='o', color='r', markersize=5)

ax.set_title('Sales Distribution per Business Sector (2020)')
ax.set_xlabel('Sales (Million)')
ax.set_ylabel('Company Sector')
ax.xaxis.grid(True)
ax.yaxis.grid(True)

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/178_202312310058.png')
plt.clf()

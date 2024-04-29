import matplotlib.pyplot as plt

data = [
    ("Model A", [8,10,13,15,17], []),
    ("Model B", [7,11,14,17,20], [5,22]),
    ("Model C", [6,12,16,19,22], [3,25]),
    ("Model D", [8,13,17,21,25], [6]),
    ("Model E", [9,14,18,22,26], [28]),
]

categories = [item[0] for item in data]
values = [item[1] for item in data]
outliers = [item[2] for item in data]

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111) 
ax.boxplot(values, vert=False, whis=1.5)
ax.yaxis.grid(True)
ax.set_yticklabels(categories, rotation=15)

for i, outlier in enumerate(outliers):
    if outlier:  
        ax.plot(outlier, [i + 1] * len(outlier), "ko")

ax.set_xlabel('Fuel Efficiency (mpg)')
ax.set_title('Fuel Efficiency Distribution of Different Truck Models in 2021')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/118_202312270030.png')
plt.clf()

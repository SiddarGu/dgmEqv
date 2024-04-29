import matplotlib.pyplot as plt
import numpy as np

data = [['Organization A',50,100,200,300,400,[]],
        ['Organization B',60,120,240,360,480,[30,500]],
        ['Organization C',80,160,320,480,640,[20,700]],
        ['Organization D',40,80,160,240,320,[5,350]],
        ['Organization E',100,200,400,600,800,[10,900]]]

reformatted_data = [i[1:6] for i in data]
outliers = [i[6] for i in data]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot()
ax.boxplot(reformatted_data, labels=[i[0] for i in data], whis=1.5)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x") 

ax.set_ylabel('Donation Amount ($)')
ax.yaxis.grid(True)
ax.xaxis.grid(True)
ax.title.set_text('Donation Amount Distribution in Charitable Organizations (2021)')

fig.autofmt_xdate(rotation=30)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/200_202312310058.png')
plt.clf()

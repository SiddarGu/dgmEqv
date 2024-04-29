
import matplotlib.pyplot as plt
import numpy as np

data = [['USA',100000,140000],['UK',80000,150000],['Germany',90000,160000],['France',70000,170000]]

country = [i[0] for i in data]
scientists = [i[1] for i in data]
engineers = [i[2] for i in data]

x = np.arange(len(country))
width = 0.35

fig = plt.figure()
ax = fig.add_subplot()
ax.bar(x - width/2, scientists, width, label='Scientists')
ax.bar(x + width/2, engineers, width, label='Engineers')

ax.set_xticks(x)
ax.set_xticklabels(country)
ax.legend()
plt.title("Number of Scientists and Engineers in four countries in 2021")
ax.annotate(str(scientists[0]), xy=(x[0] - width/2, scientists[0]/2), xytext=(x[0] - width/2, scientists[0]/2 + 1000),
            arrowprops={'arrowstyle': '-', 'connectionstyle': 'arc3, rad=0.2'})
ax.annotate(str(engineers[0]), xy=(x[0] + width/2, engineers[0]/2), xytext=(x[0] + width/2, engineers[0]/2 + 1000),
            arrowprops={'arrowstyle': '-', 'connectionstyle': 'arc3, rad=0.2'})
ax.annotate(str(scientists[1]), xy=(x[1] - width/2, scientists[1]/2), xytext=(x[1] - width/2, scientists[1]/2 + 1000),
            arrowprops={'arrowstyle': '-', 'connectionstyle': 'arc3, rad=0.2'})
ax.annotate(str(engineers[1]), xy=(x[1] + width/2, engineers[1]/2), xytext=(x[1] + width/2, engineers[1]/2 + 1000),
            arrowprops={'arrowstyle': '-', 'connectionstyle': 'arc3, rad=0.2'})
ax.annotate(str(scientists[2]), xy=(x[2] - width/2, scientists[2]/2), xytext=(x[2] - width/2, scientists[2]/2 + 1000),
            arrowprops={'arrowstyle': '-', 'connectionstyle': 'arc3, rad=0.2'})
ax.annotate(str(engineers[2]), xy=(x[2] + width/2, engineers[2]/2), xytext=(x[2] + width/2, engineers[2]/2 + 1000),
            arrowprops={'arrowstyle': '-', 'connectionstyle': 'arc3, rad=0.2'})
ax.annotate(str(scientists[3]), xy=(x[3] - width/2, scientists[3]/2), xytext=(x[3] - width/2, scientists[3]/2 + 1000),
            arrowprops={'arrowstyle': '-', 'connectionstyle': 'arc3, rad=0.2'})
ax.annotate(str(engineers[3]), xy=(x[3] + width/2, engineers[3]/2), xytext=(x[3] + width/2, engineers[3]/2 + 1000),
            arrowprops={'arrowstyle': '-', 'connectionstyle': 'arc3, rad=0.2'})

fig.set_figwidth(10)
fig.set_figheight(8)
fig.tight_layout()
plt.savefig('Bar Chart/png/592.png')
plt.clf()
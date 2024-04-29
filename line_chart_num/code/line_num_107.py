
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2016,20000,30000,40000],
                 [2017,25000,35000,45000],
                 [2018,30000,40000,50000],
                 [2019,35000,45000,55000]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

x = np.arange(data.shape[0])

ax.plot(x, data[:,1], '-o', label='Solar Energy(MWh)')
ax.plot(x, data[:,2], '-o', label='Wind Energy(MWh)')
ax.plot(x, data[:,3], '-o', label='Hydroelectric Energy(MWh)')

ax.set_xticks(x)
ax.set_xticklabels(data[:,0])

for i in range(data.shape[0]):
    ax.annotate(data[i][1], xy=(x[i], data[i][1]), color='orange')
    ax.annotate(data[i][2], xy=(x[i], data[i][2]), color='darkgreen')
    ax.annotate(data[i][3], xy=(x[i], data[i][3]), color='blue')

ax.set_title('Renewable Energy Production in the USA from 2016-2019')
ax.legend(loc='upper left')
ax.grid(alpha=0.4)

fig.tight_layout()
plt.savefig('line chart/png/111.png')
plt.clf()
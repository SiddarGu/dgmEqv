
import matplotlib.pyplot as plt
import numpy as np

data = [[2010, 100, 10, 1],
        [2011, 120, 20, 5],
        [2012, 150, 30, 10],
        [2013, 180, 50, 20],
        [2014, 220, 70, 30],
        [2015, 250, 90, 50]]

data = np.array(data)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

ax.plot(data[:,0], data[:,1], label='Facebook users(million)', color='C0')
ax.plot(data[:,0], data[:,2], label='Twitter users(million)', color='C1')
ax.plot(data[:,0], data[:,3], label='Instagram users(million)', color='C2')

ax.set_title('Social Media user growth from 2010 to 2015', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Users (million)', fontsize=14)
ax.set_xticks(data[:,0])
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

fig.tight_layout()
fig.savefig('line chart/png/450.png')
plt.clf()
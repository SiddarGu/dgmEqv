
import matplotlib.pyplot as plt
import numpy as np

data = [('2015',1.59,0.32,0.25),('2016',1.86,0.45,0.72),('2017',2.13,0.60,1.47),('2018',2.41,0.75,2.22),('2019',2.68,0.90,2.97)]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

x = [i[0] for i in data]
y1 = [i[1] for i in data]
y2 = [i[2] for i in data]
y3 = [i[3] for i in data]

ax.plot(x, y1, label='Facebook Users')
ax.plot(x, y2, label='Twitter Users')
ax.plot(x, y3, label='Instagram Users')

ax.grid(True, linestyle='-', color='0.75')
ax.set_title('Social Media User Growth from 2015-2019')
ax.set_xlabel('Year')
ax.set_ylabel('User Number')
ax.set_xticks(np.arange(len(x)))
ax.set_xticklabels(x)
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('line chart/png/53.png')
plt.clf()
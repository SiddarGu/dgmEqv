
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

data = [[2010, 100, 1000, 100000],
        [2011, 150, 2000, 200000],
        [2012, 200, 3000, 250000],
        [2013, 500, 5000, 400000],
        [2014, 800, 10000, 600000],
        [2015, 1200, 15000, 800000],
        [2016, 1800, 20000, 1000000],
        [2017, 2200, 25000, 1200000]]

x = [i[0] for i in data]
y1 = [i[1] for i in data]
y2 = [i[2] for i in data]
y3 = [i[3] for i in data]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()
ax.plot(x, y1, 'b', label='Number of users (millions)', linewidth=2)
ax.plot(x, y2, 'r', label='Number of posts (millions)', linewidth=2)
ax.plot(x, y3, 'g', label='Number of likes (millions)', linewidth=2)

ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
ax.set_title("Growth of Social Media Platforms between 2010 and 2017")
ax.set_xlabel('Year')
ax.set_ylabel('Data')

for i in range(len(x)):
    ax.annotate(str(y1[i]), xy=(x[i], y1[i]))
    ax.annotate(str(y2[i]), xy=(x[i], y2[i]))
    ax.annotate(str(y3[i]), xy=(x[i], y3[i]))

ax.legend()
fig.tight_layout()
plt.savefig('line chart/png/504.png')
plt.clf()
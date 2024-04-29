
import matplotlib.pyplot as plt
import numpy as np

data = [[2011,400000,300000,200000],
        [2012,500000,400000,300000],
        [2013,600000,500000,400000],
        [2014,700000,600000,500000],
        [2015,800000,700000,600000]]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

x = np.arange(len(data))
years = [i[0] for i in data]
soccer = [i[1] for i in data]
baseball = [i[2] for i in data]
football = [i[3] for i in data]

ax.plot(x, soccer, label='Soccer Attendance', marker='o', color='black')
ax.plot(x, baseball, label='Baseball Attendance', marker='o', color='green')
ax.plot(x, football, label='Football Attendance', marker='o', color='red')

ax.set_title("Comparison of attendance in three major sports in US from 2011 to 2015")
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_xlabel('Year')
ax.set_ylabel('Attendance')

for i,j in zip(x,soccer):
    ax.annotate(str(j), xy=(i,j), xytext=(i-0.15, j+5000), rotation=45, fontsize=8)
for i,j in zip(x,baseball):
    ax.annotate(str(j), xy=(i,j), xytext=(i-0.15, j+5000), rotation=45, fontsize=8)
for i,j in zip(x,football):
    ax.annotate(str(j), xy=(i,j), xytext=(i-0.15, j+5000), rotation=45, fontsize=8)

ax.legend(loc='upper right')
fig.tight_layout()

plt.savefig('line chart/png/323.png')

plt.clf()
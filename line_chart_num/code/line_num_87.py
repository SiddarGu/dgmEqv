

import matplotlib.pyplot as plt
import numpy as np

data = [[2000,11.2,3.4,4.2],[2001,11.8,2.8,4.8],[2002,12.5,2.6,5.8],[2003,13.2,2.3,6.2],[2004,14.2,2.6,6.5]]

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
ax.set_title("US Economic Performance in 2000s")

ax.plot(data[0],data[1],color='r', linestyle='-', linewidth=2, label='GDP')
ax.plot(data[0],data[2],color='g', linestyle='-', linewidth=2, label='Inflation Rate')
ax.plot(data[0],data[3],color='b', linestyle='-', linewidth=2, label='Unemployment Rate')

ax.set_xticks(data[0])
ax.set_xlabel('Year')
ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.01), ncol=3, shadow=True, fontsize='x-large')

for i in range(len(data[0])):
    ax.annotate(data[i], xy=(data[0][i],data[1][i]), xycoords="data", xytext=(-50,30), textcoords="offset points", rotation=30, fontsize=10, arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
    ax.annotate(data[i], xy=(data[0][i],data[2][i]), xycoords="data", xytext=(-50,30), textcoords="offset points", rotation=30, fontsize=10, arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
    ax.annotate(data[i], xy=(data[0][i],data[3][i]), xycoords="data", xytext=(-50,30), textcoords="offset points", rotation=30, fontsize=10, arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))

plt.tight_layout()
plt.savefig('line chart/png/185.png')
plt.clf()
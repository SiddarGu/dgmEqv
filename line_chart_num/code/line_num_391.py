
import matplotlib.pyplot as plt
import numpy as np

data = [[2001, 1000, 800, 200], 
        [2002, 1200, 900, 300], 
        [2003, 800, 1100, 400], 
        [2004, 1500, 1200, 500]]

x_data = [i[0] for i in data]
y_data_1 = [i[1] for i in data]
y_data_2 = [i[2] for i in data]
y_data_3 = [i[3] for i in data]

fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111)

ax.plot(x_data, y_data_1, label='No. of Suits Filed', marker='o', color='b')
ax.plot(x_data, y_data_2, label='No. of Suits Settled', marker='v', color='r')
ax.plot(x_data, y_data_3, label='No. of Suits Pending', marker='s', color='g')

plt.title('Number of Lawsuits in the US in the 21st Century')
plt.xticks(x_data, x_data, rotation=45)

for a,b in zip(x_data,y_data_1):
    ax.annotate("{:.0f}".format(b),xy=(a,b),textcoords='data')

for a,b in zip(x_data,y_data_2):
    ax.annotate("{:.0f}".format(b),xy=(a,b),textcoords='data')

for a,b in zip(x_data,y_data_3):
    ax.annotate("{:.0f}".format(b),xy=(a,b),textcoords='data')

ax.legend()
plt.tight_layout()
plt.savefig('line chart/png/128.png', dpi=128)
plt.clf()
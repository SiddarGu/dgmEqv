
import matplotlib.pyplot as plt
import numpy as np

data = [[2001, 200000,1800], [2002, 210000,1900], [2003, 220000,2000], [2004, 230000,2100], [2005, 240000,2200], [2006, 250000,2300], [2007, 260000,2400]]
x, home_price, rent = np.transpose(data)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

ax.plot(x, home_price, color='b', marker='o', label='Average Home Price')
ax.plot(x, rent, color='r', marker='o', label='Average Rent')

ax.set_title('Average Home Price and Average Rent in the US from 2001 to 2007')
ax.set_xlabel('Year')
ax.set_ylabel('Price ($)')

plt.xticks(ticks=x)
plt.legend()

for i, j in zip(x, home_price):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip(x, rent):
    ax.annotate(str(j), xy=(i, j))
plt.tight_layout()
plt.savefig('line chart/png/297.png')
plt.clf()
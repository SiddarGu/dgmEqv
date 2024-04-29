
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

year = np.array([1998, 1999, 2000, 2001])
gdp = np.array([5.3, 5.6, 5.9, 6.2])
expend = np.array([3.2, 3.5, 3.8, 4.1])
rev = np.array([2.2, 2.3, 2.4, 2.5])

ax.plot(year, gdp, label='Gross Domestic Product')
ax.plot(year, expend, label='Expenditure')
ax.plot(year, rev, label='Revenue')

ax.set_title('Changes in US GDP, Expenditure, and Revenue from 1998 to 2001')
ax.legend(loc='upper left', fontsize=12)
ax.grid(axis='y', linestyle='-')
ax.set_xticks(year)

for i, j in zip(year, gdp):
    ax.annotate(str(round(j, 2))+'trillion', xy=(i, j))

for i, j in zip(year, expend):
    ax.annotate(str(round(j, 2))+'trillion', xy=(i, j))

for i, j in zip(year, rev):
    ax.annotate(str(round(j, 2))+'trillion', xy=(i, j), rotation=45, wrap=True)

plt.tight_layout()
fig.savefig('line chart/png/336.png')
plt.clf()
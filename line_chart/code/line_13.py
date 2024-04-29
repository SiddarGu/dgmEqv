
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Increase in Tourist Numbers in the United States between 2001 and 2005')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Tourists')
ax.plot([2001, 2002, 2003, 2004, 2005], [10000, 15000, 20000, 25000, 30000], color='b', linestyle='-', marker='o', label='International Tourists')
ax.plot([2001, 2002, 2003, 2004, 2005], [20000, 25000, 30000, 35000, 40000], color='r', linestyle='-', marker='o', label='Domestic Tourists')
plt.xticks([2001, 2002, 2003, 2004, 2005])
ax.legend(loc='upper left', frameon=False)
plt.tight_layout()
plt.savefig('line chart/png/329.png')
plt.clf()
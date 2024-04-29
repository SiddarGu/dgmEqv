
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

x = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
y1 = [400, 500, 600, 700, 800, 900, 1000]
y2 = [5, 6, 7, 8, 9, 10, 12]

ax.plot(x, y1, color='b', marker='o', label='Crime Rate(per 100,000 citizens)')
ax.plot(x, y2, color='r', marker='^', label='Sentence Length(years)')

ax.set_title('Increase in Crime Rate and Sentence Length in the US from 2000-2006')
ax.set_xlabel('Year')
ax.grid(axis='y', ls='dashed', color='gray', alpha=0.5)
ax.legend(loc='upper left', fontsize='medium', frameon=True, facecolor='white')
ax.set_xticks(x)

plt.tight_layout()
plt.savefig('line chart/png/453.png',dpi=300)
plt.clf()
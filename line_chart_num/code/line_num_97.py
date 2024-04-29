
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.plot([2001, 2002, 2003, 2004], [25, 30, 28, 29], label='Tax Rate(%)')
ax.plot([2001, 2002, 2003, 2004], [8, 10, 12, 9], label='Unemployment Rate(%)')
ax.plot([2001, 2002, 2003, 2004], [1000, 1100, 1200, 1300], label='Num of Companies')

ax.set_title('Change in Tax Rate, Unemployment Rate and Number of Companies in US from 2001 to 2004')
ax.set_xlabel('Year')
ax.set_ylabel('Rate/Number')
ax.legend(loc='best')
ax.grid(True)

for i, j in zip([2001, 2002, 2003, 2004], [25, 30, 28, 29]):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip([2001, 2002, 2003, 2004], [8, 10, 12, 9]):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip([2001, 2002, 2003, 2004], [1000, 1100, 1200, 1300]):
    ax.annotate(str(j), xy=(i, j))

plt.xticks([2001, 2002, 2003, 2004])
plt.tight_layout()
plt.savefig('line chart/png/610.png')
plt.clf()
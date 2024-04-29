
import matplotlib.pyplot as plt
import numpy as np

year=[2011,2012,2013,2014,2015]
artA=[50,45,48,43,46]
artB=[60,55,58,53,56]
artC=[70,65,68,63,66]

fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111)
ax.plot(year,artA, label='Art A')
ax.plot(year,artB, label='Art B')
ax.plot(year,artC, label='Art C')

ax.set_title('Popularity of Arts in the USA from 2011 to 2015')
ax.set_xlabel('Year')
ax.set_ylabel('Popularity')

plt.xticks(np.arange(min(year), max(year)+1, 1.0))
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/310.png')
plt.close()
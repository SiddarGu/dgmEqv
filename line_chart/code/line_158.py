
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
ax = plt.subplot()

x = np.array([2001,2002,2003,2004,2005,2006,2007])
y1 = np.array([10,12,15,16,14,13,11])
y2 = np.array([5,6,8,10,9,7,8])

ax.plot(x, y1, color='green',label='Donations (million dollars)')
ax.plot(x, y2, color='red',label='Volunteers (millions)')

ax.set_title('Global Nonprofit Donations and Volunteers from 2001 to 2007')
ax.set_xlabel('Year')
ax.set_ylabel('Amount')

plt.xticks(x)
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig('line chart/png/253.png')
plt.clf()
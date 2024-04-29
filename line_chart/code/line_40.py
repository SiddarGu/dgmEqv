
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(1,1,1)

data = np.array([[2001, 10, 1], [2002, 11, 2], [2003, 13, 3], [2004, 14, 4], [2005, 15, 5], [2006, 17, 8], [2007, 18, 10]])

x = data[:,0]
y1 = data[:,1]
y2 = data[:,2]

ax.plot(x, y1, color='blue', label='Average Temperature (degrees Celsius)')
ax.plot(x, y2, color='red', label='Sea Level Rise (millimeters)')

ax.set_title('Global Temperature and Sea Level Rise from 2001 to 2007')
ax.legend(loc='upper left', bbox_to_anchor=(1,1), borderaxespad=1)

ax.set_xticks(x)

plt.tight_layout()
plt.savefig('line chart/png/153.png')
plt.clf()
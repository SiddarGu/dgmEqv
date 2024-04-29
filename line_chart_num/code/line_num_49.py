
import matplotlib.pyplot as plt
import numpy as np

data = [[2001, 200, 50],
        [2002, 220, 60],
        [2003, 240, 65],
        [2004, 260, 70],
        [2005, 280, 75],
        [2006, 300, 80],
        [2007, 320, 85],
        [2008, 340, 90]]

data = np.array(data)

x = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]

plt.figure(figsize=(10, 6))
plt.plot(x, y1, marker='o', label='Average House Price')
plt.plot(x, y2, marker='o', label='Average Rent Price')

for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='top', fontsize=10)

plt.title('US Real Estate Market Development from 2001 to 2008')
plt.xlabel('Year')
plt.ylabel('Price (thousand dollars)')
plt.xticks(x)
plt.legend(loc='upper left', prop={'size': 10})

plt.tight_layout()
plt.savefig('line chart/png/416.png')
plt.clf()
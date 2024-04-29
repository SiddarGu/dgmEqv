
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2009, 2010, 2011, 2012])
y1 = np.array([10000, 11000, 13000, 15000])
y2 = np.array([8000, 9000, 10000, 13000])

fig = plt.figure(figsize=(10, 8))
plt.title('Changes in Crime and Conviction Rates in the United States from 2009 to 2012')

plt.grid(True, alpha=0.7)

plt.plot(x, y1, color='red', linestyle='dashed', marker='.', markerfacecolor='green', markersize=10,label='Number of Crimes')
plt.plot(x, y2, color='blue', linestyle='dashed', marker='.', markerfacecolor='orange', markersize=10, label='Number of Convictions')

plt.xlabel('Year')
plt.ylabel('Number')

plt.xticks(x)

for a, b in zip(x, y1):
    plt.text(a, b, '{}'.format(b), ha='center', va='bottom', fontsize=10)

for a, b in zip(x, y2):
    plt.text(a, b, '{}'.format(b), ha='center', va='bottom', fontsize=10)

plt.legend(loc='best', fontsize=10)

plt.tight_layout()
plt.savefig('line chart/png/573.png')
plt.clf()
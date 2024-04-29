
import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([2010,2011,2012,2013,2014,2015,2016])
y1_data = np.array([90,92,94,95,97,98,99])
y2_data = np.array([80,81,82,83,84,85,86])

fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot(111)
ax.plot(x_data, y1_data, label='Health Insurance', marker='o')
ax.plot(x_data, y2_data, label='Clean Water', marker='^')

for x, y1, y2 in zip(x_data, y1_data, y2_data):
    ax.annotate(y1, xy=(x, y1), xytext=(0, 6), 
        textcoords='offset points', ha='center', va='bottom')
    ax.annotate(y2, xy=(x, y2), xytext=(0, 6), 
        textcoords='offset points', ha='center', va='top')

plt.xticks(x_data)
plt.xlabel('Year')
plt.title('Increase of Health Insurance Coverage and Access to Clean Water in the US from 2010 to 2016')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/422.png')
plt.clf()
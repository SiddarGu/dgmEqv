
import matplotlib.pyplot as plt
import numpy as np

year = np.array([2011, 2012, 2013, 2014, 2015, 2016])
smartphone = np.array([100, 300, 400, 500, 600, 700])
tablet = np.array([50, 80, 120, 150, 180, 200])
computer = np.array([20, 50, 80, 100, 120, 150])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()
ax.plot(year, smartphone, label='Smartphone', marker='o')
ax.plot(year, tablet, label='Tablet', marker='o')
ax.plot(year, computer, label='Computer', marker='o')
ax.set_title('Sales of Smartphone, Tablet and Computer from 2011 to 2016')
ax.set_xlabel('Year')
ax.set_ylabel('Sales')
ax.legend(loc='upper left')
ax.grid(True)
ax.set_xticks(year)
plt.tight_layout()
plt.savefig('line chart/png/25.png')
plt.clf()
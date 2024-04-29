

import matplotlib.pyplot as plt
import numpy as np

# prepare data
data = [[2000, 50, 2, 0],
        [2001, 53, 4, 0],
        [2002, 55, 6, 1],
        [2003, 57, 8, 2],
        [2004, 58, 10, 4],
        [2005, 60, 12, 5],
        [2006, 62, 14, 8],
        [2007, 64, 16, 10]]

data = np.array(data)
year = data[:, 0]
nuclear = data[:, 1]
wind = data[:, 2]
solar = data[:, 3]

# plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
plt.plot(year, nuclear, label='Nuclear energy(TWh)')
plt.plot(year, wind, label='Wind energy(TWh)')
plt.plot(year, solar, label='Solar energy(TWh)')
plt.xticks(year)
ax.annotate('Nuclear: 50', xy=(2000, 50), xytext=(2000, 55))
ax.annotate('Wind: 2', xy=(2000, 2), xytext=(2000, 7))
ax.annotate('Solar: 0', xy=(2000, 0), xytext=(2000, 5))
plt.xlabel('Year')
plt.ylabel('TWh')
plt.grid()
plt.title('Renewable energy sources growth in comparison to Nuclear energy in the US from 2000 to 2007')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig('line chart/png/338.png')
plt.clf()
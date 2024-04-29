
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

country = ['USA','UK','Germany','France']
theater = [20,25,18,23]
cinema = [30,35,28,33]
museum = [40,45,38,43]

width = 0.2
x = np.arange(len(country))

ax.bar(x-width, theater, width=width, label='Theater Visits')
ax.bar(x, cinema, width=width, label='Cinema Visits')
ax.bar(x+width, museum, width=width, label='Museums Visits')

ax.set_xticks(x)
ax.set_xticklabels(country, rotation=90, wrap=True)
ax.legend(loc='upper right')

ax.set_title('Number of visits to theaters, cinemas and museums in four countries in 2021')

plt.tight_layout()
plt.savefig('bar chart/png/479.png')
plt.clf()
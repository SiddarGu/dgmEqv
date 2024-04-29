
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

countries = ['USA', 'UK', 'Germany', 'France']
small_businesses = [2500, 1800, 2700, 2000]
midsize_businesses = [1500, 1200, 1700, 1400]
large_businesses = [700, 900, 800, 1000]

x_pos = np.arange(len(countries))

ax.bar(x_pos, small_businesses, width=0.2, bottom=None, align='edge', label='Small Businesses')
ax.bar(x_pos + 0.2, midsize_businesses, width=0.2, bottom=None, align='edge', label='Midsize Businesses')
ax.bar(x_pos + 0.4, large_businesses, width=0.2, bottom=None, align='edge', label='Large Businesses')

ax.set_title("Businesses by size in four countries in 2021")

ax.set_xticks(x_pos)
ax.set_xticklabels(countries)
ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig('bar chart/png/10.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

# data
country = ['USA', 'UK', 'Germany', 'France']
retail_stores = [500, 400, 300, 400]
online_stores = [1500, 1200, 1000, 1300]

# create figure
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot()

# draw bar chart
x = np.arange(len(country))
ax.bar(x - 0.3/2, retail_stores, 0.3, label='Retail Stores')
ax.bar(x + 0.3/2, online_stores, 0.3, label='Online Stores')

# set ticks
ax.set_xticks(x)
ax.set_xticklabels(country, rotation=45, fontsize=12, wrap=True)

# add title and legend
ax.set_title('Number of Retail and Online Stores in four countries in 2021')
ax.legend()

# save img
plt.tight_layout()
plt.savefig('bar chart/png/289.png')

# clear figure
plt.clf()
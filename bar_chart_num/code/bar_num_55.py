
import matplotlib.pyplot as plt
import numpy as np

# define data 
region = ('Asia','North America','South America','Europe')
number = [120,100,80,90]
capital = [500,400,300,350]

# create figure 
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# plot data
ax.bar(region, number, label='Number of Businesses (thousand)')
ax.bar(region, capital, bottom=number, label='Startup Capital (million)')

# set xticks
ax.set_xticks(np.arange(len(region)))
ax.set_xticklabels(region)

# set legend 
ax.legend(loc="upper right")

# set title 
ax.set_title('Number of Businesses and Startup Capital in four regions in 2021')

# annotate 
for n, c, r in zip(number, capital, region):
    ax.annotate(str(n+c), xy=(r, n+c/2), ha='center', va='center')

# save image
plt.tight_layout()
plt.savefig('Bar Chart/png/304.png')

# clear state
plt.clf()
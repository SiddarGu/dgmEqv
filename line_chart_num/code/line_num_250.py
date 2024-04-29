
import matplotlib.pyplot as plt
import numpy as np

region = ['North America','South America','Europe','Asia','Africa','Australia']
number = [900,800,1200,1000,500,300]

fig,ax = plt.subplots(figsize=(10,6))
plt.plot(region, number, color='#ff7f50', marker='o', linewidth=3, markersize=10)

ax.set_title("Number of Tourists Visiting Different Regions in 2021")
for i in range(len(number)):
    ax.annotate(number[i], (region[i],number[i]))
ax.set_xticks(region)

plt.tight_layout()
plt.savefig('line chart/png/81.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12,8))

country = ['USA','UK','Germany','France']
museums = [150,170,130,140]
theatres = [180,200,150,190]
galleries = [220,250,190,220]

bar_width = 0.25

bars1 = ax.bar(country, museums, width = bar_width, color = '#b5ffb9', edgecolor = 'white', label = 'Museums')
bars2 = ax.bar(np.arange(len(country))+bar_width, theatres, width = bar_width, color = '#f9bc86', edgecolor = 'white', label = 'Theatres')
bars3 = ax.bar(np.arange(len(country))+bar_width*2, galleries, width = bar_width, color = '#a3acff', edgecolor = 'white', label = 'Galleries')

ax.set_title('Number of Museums, Theatres and Galleries in four countries in 2021')
ax.set_xticks(np.arange(len(country))+bar_width)
ax.set_xticklabels(country)
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend()

for bar1, bar2, bar3 in zip(bars1, bars2, bars3):
    yval = bar1.get_height() + bar2.get_height() + bar3.get_height()
    ax.annotate('{}'.format(yval),
            xy=(bar1.get_x() + bar1.get_width() / 2, yval),
            xytext=(0, 3), 
            textcoords="offset points",
            ha='center', va='bottom', rotation = 90, wrap=True)

plt.tight_layout()
plt.savefig('Bar Chart/png/444.png')
plt.clf()
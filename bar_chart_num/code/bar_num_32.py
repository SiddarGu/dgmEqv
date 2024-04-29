

import matplotlib.pyplot as plt
import numpy as np

# set data
countries = ('USA', 'UK', 'Germany', 'France')
galleries = (20, 25, 15, 18)
museums = (30, 40, 35, 32)
theaters = (50, 60, 45, 55)

# draw figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# plot
x = np.arange(len(countries))
width = 0.2

ax.bar(x, galleries, width, label='Galleries')
ax.bar(x + width, museums, width, label='Museums')
ax.bar(x + 2*width, theaters, width, label='Theaters')

# set ticks
ax.set_xticks(x + width)
ax.set_xticklabels(countries)
ax.set_ylabel('Number of Facilities')

# annotate labels
for a,b in zip(x, galleries):
    ax.annotate(str(b), xy=(a, b), xytext=(0, 3), 
                textcoords='offset points', ha='center', va='bottom')
for a,b in zip(x, museums):
    ax.annotate(str(b), xy=(a+width, b), xytext=(0, 3), 
                textcoords='offset points', ha='center', va='bottom')
for a,b in zip(x, theaters):
    ax.annotate(str(b), xy=(a+2*width, b), xytext=(0, 3), 
                textcoords='offset points', ha='center', va='bottom')

# legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07),
          fancybox=True, shadow=True, ncol=3)

# set title
fig.suptitle('Arts and Culture facilities in four countries in 2021', fontsize=14)

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('Bar Chart/png/211.png')

# clear figure
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7,5))
categories = ['Museums', 'Art Galleries', 'Theatres']

USA = [50, 100, 60]
UK = [45, 90, 55]
Germany = [40, 80, 50]
France = [35, 70, 45]

x_pos = np.arange(len(categories))
width = 0.2

ax = plt.subplot()
ax.bar(x_pos - width, USA, width, label='USA')
ax.bar(x_pos, UK, width, label='UK')
ax.bar(x_pos + width, Germany, width, label='Germany')
ax.bar(x_pos + 2*width, France, width, label='France')

ax.set_xticks(x_pos)
ax.set_xticklabels(categories)
ax.set_ylabel('Number of venues')
ax.set_title('Number of arts and cultural venues in four countries in 2021')

ax.legend()

for x, y in zip(x_pos, USA):
    ax.annotate('{}'.format(y), 
            xy=(x - width, y + 1),
            xytext=(0, 3),  
            textcoords="offset points",
            rotation=90,
            ha='center',
            va='bottom')

for x, y in zip(x_pos, UK):
    ax.annotate('{}'.format(y), 
            xy=(x, y + 1),
            xytext=(0, 3),  
            textcoords="offset points",
            rotation=90,
            ha='center',
            va='bottom')

for x, y in zip(x_pos, Germany):
    ax.annotate('{}'.format(y), 
            xy=(x + width, y + 1),
            xytext=(0, 3),  
            textcoords="offset points",
            rotation=90,
            ha='center',
            va='bottom')

for x, y in zip(x_pos, France):
    ax.annotate('{}'.format(y), 
            xy=(x + 2*width, y + 1),
            xytext=(0, 3),  
            textcoords="offset points",
            rotation=90,
            ha='center',
            va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/154.png')
plt.clf()


import matplotlib.pyplot as plt
import numpy as np

# Create figure 
fig = plt.figure()
ax = fig.add_subplot(111)

# Set data
region = ['North America', 'South America', 'Europe', 'Asia']
veg_prod = [4000, 5000, 3000, 4500]
fruit_prod = [2000, 3000, 1500, 2500]

# Create Bar Chart
x = np.arange(len(region))
width = 0.35
rects1 = ax.bar(x - width/2, veg_prod, width, label='Vegetable Production (tonnes)')
rects2 = ax.bar(x + width/2, fruit_prod, width, label='Fruit Production (tonnes)')

# Set labels and title
ax.set_title('Vegetable and Fruit Production in Four Regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(region)
ax.legend()

# Annotate labels
for rect in rects1:
    height = rect.get_height()
    ax.annotate('{0}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center', va='bottom')
for rect in rects2:
    height = rect.get_height()
    ax.annotate('{0}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center', va='bottom')

# Resize figure
fig.set_figwidth(10)
fig.set_figheight(6)
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/547.png')

# Clear figure
plt.clf()
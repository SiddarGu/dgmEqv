
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

# Set data
x = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
y1 = np.array([500, 550, 600, 650, 700, 750, 800, 850])
y2 = np.array([800, 850, 900, 950, 1000, 1050, 1100, 1150])

# Plot the data
ax.plot(x, y1, color='tab:blue', label='Criminal Cases Filed')
ax.plot(x, y2, color='tab:orange', label='Civil Cases Filed')

# Set x ticks
ax.set_xticks(x)

# Set title
ax.set_title('Trend of Cases Filed in US Courts in 2010-2017')

# Set legend
ax.legend(loc=2, ncol=2, fontsize='large')

# Annotate points
for x, y1, y2 in zip(x, y1, y2):
    ax.annotate(f'{y1}', xy=(x, y1), xytext=(5, 5), textcoords='offset points', fontsize='large')
    ax.annotate(f'{y2}', xy=(x, y2), xytext=(5, 5), textcoords='offset points', fontsize='large')

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/537.png')

# Clear current image state
plt.clf()
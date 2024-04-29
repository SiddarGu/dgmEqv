
import matplotlib.pyplot as plt
import numpy as np

# Set data
year = np.array([2010,2011,2012,2013,2014])
GE = np.array([1000,1100,1200,1300,1400])
TR = np.array([800,900,1100,1000,1200])

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

# Plot
ax.plot(year, GE, label='Government Expenditure(billion dollars)', color='b', linestyle='dashed', linewidth=2)
ax.plot(year, TR, label='Tax Revenue(billion dollars)', color='g', linestyle='solid', linewidth=2)

# Set x ticks
ax.set_xticks(year)

# Set title, legend and grid
ax.set_title('Government Expenditure and Tax Revenue from 2010 to 2014')
ax.legend(loc='best')
ax.grid()

# Annotate
for x, y in zip(year, GE):
    plt.annotate('%.2f' % y, xy=(x,y), xytext=(x-0.2, y+50))
for x, y in zip(year, TR):
    plt.annotate('%.2f' % y, xy=(x,y), xytext=(x-0.2, y+50))

# Resize plot
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/239.png')

# Clear current image state
plt.clf()
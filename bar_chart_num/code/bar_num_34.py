
import matplotlib.pyplot as plt 
import numpy as np

# create figure object
fig = plt.figure(figsize=(12, 8))

# define array of data
region = np.array(['North America', 'Europe', 'Asia', 'Africa'])
donations = np.array([500, 400, 300, 200])
volunteers = np.array([4500, 3000, 2000, 1000])

# draw a bar chart
ax = fig.add_subplot()
ax.bar(region, donations, label='Donations', width=0.3, color='b')
ax.bar(region, volunteers, bottom=donations, label='Volunteers', width=0.3, color='r')

# annotate the value of each data point
for i in range(len(region)):
    ax.annotate(str(donations[i])+'\n'+str(volunteers[i]), xy=(region[i], donations[i]+volunteers[i]/2), ha='center', va='center')

# set title
ax.set_title('Charitable donations and volunteers in four regions in 2021')

# set x ticks
ax.set_xticks(region)

# add legend
ax.legend()

# optimize layout
plt.tight_layout()

# save the figure
plt.savefig('Bar Chart/png/318.png')

# clear the current image state
plt.clf()
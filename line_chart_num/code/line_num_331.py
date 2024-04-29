

import matplotlib.pyplot as plt
import numpy as np

# create figure before plotting
fig = plt.figure(figsize=(12,6)) 
ax = fig.add_subplot(111)

# plot the data
x = np.arange(6)
months = ["January","February","March","April","May","June"]
train_travelers = [1000,1200,1400,1600,1800,2000]
plane_travelers = [2000,2500,3000,2700,2500,3000]
bus_travelers = [3000,3500,4000,3300,3500,3800]
ax.plot(x,train_travelers,label="Train Travelers",marker='o')
ax.plot(x,plane_travelers,label="Plane Travelers",marker='o')
ax.plot(x,bus_travelers,label="Bus Travelers",marker='o')

# set the xticks
plt.xticks(x,months)

# add the value of each data point directly on the figure
for a,b in zip(x,train_travelers):
    ax.annotate('{}'.format(b),xy=(a,b),xytext=(0,2),textcoords='offset points',fontsize=10)
for a,b in zip(x,plane_travelers):
    ax.annotate('{}'.format(b),xy=(a,b),xytext=(0,2),textcoords='offset points',fontsize=10)
for a,b in zip(x,bus_travelers):
    ax.annotate('{}'.format(b),xy=(a,b),xytext=(0,2),textcoords='offset points',fontsize=10)

# set the background grids
ax.grid(linestyle='--',color='black',alpha=0.3)

# set the title
ax.set_title("Monthly Travelers Statistics in Different Transportation Modes in 2021")

# set the legend
ax.legend(loc='upper left')

# automatically resize the image
plt.tight_layout()

# save the figure
plt.savefig("line chart/png/539.png")

# clear the current image state
plt.clf()
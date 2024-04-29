
import matplotlib.pyplot as plt
import numpy as np

# set the figure size
plt.figure(figsize=(12,8))

# set the subplot
ax = plt.subplot(111)

# get the data
data = np.array([[2010,1000,1200,1500],
                 [2011,1100,1400,1400],
                 [2012,1300,1400,1300],
                 [2013,1200,1300,1100],
                 [2014,1400,1200,1000]])

# get the year and population data
year = data[:,0]
cityA = data[:,1]
cityB = data[:,2]
cityC = data[:,3]

# plot the line chart
plt.plot(year,cityA,label='City A',marker='^', markersize=8)
plt.plot(year,cityB,label='City B',marker='o', markersize=8)
plt.plot(year,cityC,label='City C',marker='s', markersize=8)

# draw the background grid
plt.grid(alpha=0.3)

# annotate the value of each data point
for i,j in zip(year,cityA):
    ax.annotate(str(j),xy=(i,j+50),fontsize=14)
for i,j in zip(year,cityB):
    ax.annotate(str(j),xy=(i,j+50),fontsize=14)
for i,j in zip(year,cityC):
    ax.annotate(str(j),xy=(i,j+50),fontsize=14)

# x-axis
plt.xticks(year,year,rotation=90)

# y-axis
plt.ylabel('Population',fontsize=14)

# title
plt.title('Population Change in Three Cities from 2010 to 2014',fontsize=16)

# legend
plt.legend(loc='upper right',fontsize=14)

# adjust image size
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/67.png')

# clear the current image state
plt.clf()
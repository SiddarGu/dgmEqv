import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Define data
data_labels = ['Installed Capacity (MW)','Electricity Generation (GWh)','Carbon Emissions (Million Metric Tons)']
line_labels = ['Coal','Natural Gas','Nuclear','Hydro','Solar','Wind','Biomass','Geothermal','Other']
data = np.array([[4000,10000,200],
                 [3000,8000,100],
                 [2500,5000,50],
                 [2000,6000,0],
                 [1500,4000,10],
                 [1000,3000,5],
                 [500,1000,1],
                 [300,500,0],
                 [100,200,0]])

fig = plt.figure(figsize=(25, 15))

# ax1 for bar chart
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], color ='b', width=0.4)
ax1.set_ylabel(data_labels[0],color='b')

# ax2 for first line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color ='g')
ax2.set_ylabel(data_labels[1],color='g')

# ax3 for second line chart
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color ='r')
ax3.set_ylabel(data_labels[2],color='r')

# Move the last y-axis spine over to the right by 20% of the width of the axes
ax3.spines['right'].set_position(('outward', 60))

ax1.set_title("Energy and Utilities Analysis: Capacity, Generation, and Emissions")

# set auto-locator
ax1.yaxis.set_major_locator(mpl.ticker.AutoLocator())
ax2.yaxis.set_major_locator(mpl.ticker.AutoLocator())
ax3.yaxis.set_major_locator(mpl.ticker.AutoLocator())

# add grid
ax1.grid()

# add legend
ax1.legend(["Installed Capacity (MW)"], loc='upper left')
ax2.legend(["Electricity Generation (GWh)"], loc='upper center')
ax3.legend(["Carbon Emissions (Million Metric Tons)"], loc='upper right')

# automatically adjust subplot params
plt.tight_layout()

# save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/304_202312311430.png")

# clear the current figure's content
plt.clf()

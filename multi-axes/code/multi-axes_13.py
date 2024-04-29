
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Number of Viewers (Millions)','Revenue (Millions of Dollars)','Average Viewing Time (Minutes)']
line_labels = ['Movies','Concerts','Sporting Events','Theme Parks','Live Shows','Music Festivals','Gaming','Online Streaming','Theaters','Las Vegas Shows','Amusement Parks']
data = np.array([[190,2750,112],
                 [54,810,76],
                 [84,1250,102],
                 [105,1720,90],
                 [68,910,58],
                 [44,680,75],
                 [125,2180,183],
                 [230,3750,168],
                 [65,1040,106],
                 [32,490,84],
                 [98,1520,86]])

plot_types = ['bar','line','area','scatter']

fig = plt.figure(figsize = (15, 10))
ax1 = fig.add_subplot(111)

# plot the first column data
ax1.bar(line_labels, data[:,0], width = 0.1, alpha = 0.5, color = 'r')
ax1.set_ylabel(data_labels[0], color = 'r', fontsize = 16)
ax1.set_xlabel('Category', fontsize = 16)
ax1.tick_params(axis = 'y', colors = 'r')

# plot the second column data
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], '-o', color = 'b', alpha = 0.6)
ax2.set_ylabel(data_labels[1], color = 'b', fontsize = 16)
ax2.tick_params(axis = 'y', colors = 'b')

# plot the third column data
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], '-s', color = 'g', alpha = 0.6)
ax3.set_ylabel(data_labels[2], color = 'g', fontsize = 16)
ax3.tick_params(axis = 'y', colors = 'g')
ax3.spines['right'].set_position(('axes', 1.1))

# draw the background grids
ax1.grid(alpha = 0.3)

# adjust the range of all y-axes
ax1.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()

# set the title of the figure
ax1.set_title('Sports and Entertainment Viewers and Revenue Analysis', fontsize = 20)

# automatically resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/43_2023122261325.png')

# clear the figure
plt.clf()
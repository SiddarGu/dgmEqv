import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# transforming the given data 
data_labels = ['Artworks Sold', 'Revenue (Millions of Dollars)', 'Average Artwork Price (Thousands of Dollars)']
line_labels = ['Picasso', 'Van Gogh', 'Monet', 'Da Vinci', 'Warhol', 'Rembrandt', 'Kandinsky', 'Matisse', 'Kahlo', 'Dali']
data = np.array([[1200,630,525], [950,475,500], [850,425,500], [780,390,500], [1650,825,500], [700,350,500], [1200,600,500], [1000,500,500], [950,475,500],[850,425,500]])

# create figure
fig = plt.figure(figsize=(24,10)) 
ax1 = fig.add_subplot(111)

# plot bar chart 
ax1.bar(line_labels, data[:,0], color='b', alpha=0.7, label=data_labels[0])

# plot line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', label=data_labels[1])

# plot scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='g', label=data_labels[2])

# plot area chart
ax4 = ax1.twinx() 
ax4.fill_between(line_labels, data[:,0], color='y', alpha=0.4, label=data_labels[0]) 

# label all axes and match their colors
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='r')
ax3.set_ylabel(data_labels[2], color='g')

# Use spine() and set_position() for ax3, ax4 to seperate different y-axes.
ax3.spines['right'].set_position(('outward', 60))
ax4.spines['right'].set_position(('outward', 120))

# show the legends of all plots at different positions
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
ax4.legend(loc='lower left')

# Drawing techniques, background grids
ax1.grid()


# Title of the figure
plt.title('Cultural and Economic Impact of Artists')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/240_202312311051.png')

# Clear the current figure
plt.clf()

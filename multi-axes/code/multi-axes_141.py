import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

raw_data = '''City,Number of Houses Sold,Average Price (Thousands of Dollars),Average Days on Market,Number of Listings
New York,500,859,56,1500
Los Angeles,650,1250,60,2250
Chicago,480,320,35,930
Houston,620,295,32,1200
Philadelphia,450,247,37,899
Phoenix,700,308,27,2000
San Antonio,600,185,29,1300
San Diego,580,680,67,1200
Dallas,610,365,43,1500
San Jose,400,1472,72,800'''

lines = raw_data.split("\n")

# Spilt the data to labels and data
data_labels = lines[0].split(",")[1:]
line_labels = [l.split(",")[0] for l in lines[1:]]

# Get numerical ndarray by transforming the rest data
data = np.array([[float(val) for val in l.split(",")[1:]] for l in lines[1:]])

# Make the figure layout
fig = plt.figure(figsize=(18,10))
ax1 = fig.add_subplot(111)

# Set a color cycle for plots
colors = ['b', 'g', 'r', 'c']
ax1.set_prop_cycle(color=colors)

# Initialize the positions for the bars
bar_positions = np.arange(len(line_labels))

# Plot loop
for i in range(data.shape[1]):
    if i == 0:
        ax1.plot(line_labels, data[:,i], label=data_labels[i])
        ax1.set_ylabel(data_labels[i], color=colors[i])
        ax1.yaxis.label.set_color(colors[i])
    elif i == 1:
        ax2 = ax1.twinx()
        ax2.bar(bar_positions-0.2, data[:,i], width=0.4, color=colors[i], alpha=0.6, label=data_labels[i])
        ax2.set_ylabel(data_labels[i], color=colors[i])
        ax2.yaxis.label.set_color(colors[i])
    elif i == 2:
        ax3 = ax1.twinx()
        ax3.scatter(line_labels, data[:,i], color=colors[i], label=data_labels[i])
        ax3.spines['right'].set_position(('outward', 60))
        ax3.set_ylabel(data_labels[i], color=colors[i])
        ax3.yaxis.label.set_color(colors[i])
    elif i == 3:
        ax4 = ax1.twinx()
        ax4.fill_between(line_labels, 0, data[:,i], color=colors[i], alpha=0.3, label=data_labels[i])
        ax4.spines['right'].set_position(('outward', 120))
        ax4.set_ylabel(data_labels[i], color=colors[i])
        ax4.yaxis.label.set_color(colors[i])

# Set the title and x-axis labels
ax1.set_title('Comparative Analysis of Real Estate Market across Major U.S. Cities')
ax1.set_xlabel('Cities')

# Show legends distinctly
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(bbox_to_anchor=(0.5, 0.96, 0.5, 0.4))
ax4.legend(bbox_to_anchor=(1.1, 0.96, 0.5, 0.4))

# Adjust the range of all y-axes using Autolocator
for ax in [ax1, ax2, ax3, ax4]:
    ax.yaxis.set_major_locator(AutoLocator())

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/205_202312311051.png')

# Clear the current image for next plot
plt.clf()

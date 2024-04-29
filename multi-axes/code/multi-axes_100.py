import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Transforming given data into desired format
data_labels = ["Number of International Tourists", "Hotel Occupancy Rate (%)", "Average Hotel Room Rate ($)"]
data = np.array([
                 [258354,78,179],
                 [193057,82,209],
                 [183123,74,162],
                 [87142,80,192],
                 [66531,70,156],
                 [54098,62,142]
                 ])
line_labels = ["Europe", "North America", "Asia", "Oceania", "South America", "Africa"]

colors = ['r', 'g', 'b']
plot_types = ["bar", "line", "scatter"]

fig = plt.figure(figsize=(25,15))  
ax = fig.add_subplot(111)  

# Plotting data for multiple axes
for i in range(data.shape[1]):
    if i == 0: 
        ax1 = ax
    else:
        ax1 = ax.twinx()

    if plot_types[i] == "bar":
        width = 0.2  
        ax1.bar(np.arange(len(data[:,i])) + i*width, data[:,i], color=colors[i], alpha=0.6, width=width)
    elif plot_types[i] == "line":
        ax1.plot(line_labels, data[:,i], color=colors[i])
    else:
        ax1.scatter(line_labels, data[:,i], color=colors[i])
    
    ax1.set_ylabel(data_labels[i], color=colors[i])
    
    ax1.yaxis.label.set_color(colors[i])
    ax1.spines['right'].set_color(colors[i])
    ax1.spines['right'].set_position(('outward', 60*i))

    ax1.xaxis.grid()

    if i != 0:
        ax1.yaxis.set_major_locator(AutoLocator())
        
    plt.legend([data_labels[i]], loc='upper left', bbox_to_anchor=(1.1, 1-0.1*i))
    
plt.title('International Tourism and Hotel Performance by Region')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/303_202312311430.png')
plt.clf() 

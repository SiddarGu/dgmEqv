# necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Given data
data_labels = ["Research Funding (Millions of Dollars)", "Number of Patents Filed", "Number of Scientific Publications", "Number of Engineering Graduates"]
line_labels = ["Chemistry","Physics","Biology","Computer Science","Civil Engineering","Mechanical Engineering","Electrical Engineering","Materials Science","Environmental Science","Chemical Engineering","Astronomy"]
data = np.array([[50,100,500,2000],[60,150,600,2500],[70,200,700,3000],[80,250,800,3500],[90,300,900,4000],[100,350,1000,4500],[110,400,1100,5000],[120,450,1200,5500],[130,500,1300,6000],[140,550,1400,6500],[150,600,1500,7000]])

# Create Figure and Subplots
fig, ax1 = plt.subplots(figsize=(20,10))

# Initial settings
color_list = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
axes = [ax1]
plot_types = ['bar', 'scatter', 'fill_between', 'bar']

# Plotting each ax
for i in range(data.shape[1]):
    if i > 0: # creating new ax based on the first plot
        axn = ax1.twinx()
        axn.spines['right'].set_position(('outward', 60*(i-1)))
        axes.append(axn)
    else:
        axn = ax1
        
    if plot_types[i] == 'bar':
        axes[i].bar(line_labels, data[:, i], color=color_list[i], alpha=0.6, label=data_labels[i])
    elif plot_types[i] == 'scatter':
        axes[i].scatter(line_labels, data[:, i], color=color_list[i], label=data_labels[i])
    elif plot_types[i] == 'fill_between':
        axes[i].fill_between(line_labels, data[:, i], color=color_list[i], alpha=0.4, label=data_labels[i])

    # Setting the y-labels and its colors
    axes[i].set_ylabel(data_labels[i], color=color_list[i])
    axes[i].tick_params(axis='y', labelcolor=color_list[i])

# Title and grid
plt.title('Trends in Science and Engineering: Funding, Patents, Publications, and Graduates')
ax1.grid(True)

# Legend and save figure
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/265_202312311430.png')

# Clear the current figure's state
plt.clf()

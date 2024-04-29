import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

data_str = '''Year,Number of Cases Filed,Number of Cases Resolved,Percent of Cases Resolved
2018,34600,32000,92
2019,36700,34000,93
2020,38100,35000,92
2021,38500,35500,92'''
plot_types = ['line', 'area', 'bar']
data_lines = data_str.split("\n") 
line_labels = [line.split(",")[0] for line in data_lines[1:]] 
data = np.array([[int(num) for num in line.split(",")[1:]] for line in data_lines[1:]]) 
data_labels = data_lines[0].split(",")[1:] 

fig = plt.figure(figsize=(24,12)) 
ax1 = fig.add_subplot(111) 
colors = ['g', 'r', 'b'] 
ax_list = [ax1] 
for i in range(data.shape[1]): 
    if plot_types[i%len(plot_types)] == "bar": 
        ax_list[i].bar(np.arange(len(line_labels))+i*0.25, data[:, i], width=0.25, color=colors[i%len(colors)], alpha=0.5, label=data_labels[i]) 
    elif plot_types[i%len(plot_types)] == "area": 
        ax_list[i].fill_between(line_labels, data[:, i], color=colors[i%len(colors)], alpha=0.3, label=data_labels[i]) 
    elif plot_types[i%len(plot_types)] == "line": 
        ax_list[i].plot(line_labels, data[:, i], color=colors[i%len(colors)], label=data_labels[i]) 
    ax_list[i].set_ylabel(data_labels[i], color=colors[i%len(colors)]) 
    ax_list[i].tick_params(axis='y', colors=colors[i%len(colors)]) 
    ax_list[i].grid(True) 
    ax_list[i].yaxis.set_major_locator(AutoLocator()) 
    ax_list[i].legend(loc='upper left') 
    if i >= 1: 
        ax_list[i].spines['right'].set_position(('outward', (i-1)*60)) 
    if i < data.shape[1] - 1: 
        ax_list.append(ax1.twinx())

plt.title('Yearly Analysis of Legal Cases: Filed, Resolved and Percent Resolved') 
plt.tight_layout() 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/89_2023122292141.png') 
plt.cla() 
plt.clf() 

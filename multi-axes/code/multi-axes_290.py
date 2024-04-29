import matplotlib.pyplot as plt
import numpy as np

data_string = """Year,Total Production (tons),Average Price per Ton (USD),Yield (tons per acre),Crops Sold
2010,150000,120,2.5,140000
2011,152000,125,2.6,142000
2012,155000,130,2.7,145000
2013,158000,135,2.8,148000
2014,160000,140,2.9,151000
2015,165000,145,3.0,155000
2016,170000,150,3.1,160000
2017,175000,155,3.2,165000
2018,180000,160,3.3,170000
2019,185000,165,3.4,175000"""
plot_types = ["bar", "line", "line", "area"]

# Transform data
lines = data_string.split('\n')
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines[1:]])
data_labels = lines[0].split(',')[1:]

# Plot
fig = plt.figure(figsize=(24,13))
ax1 = fig.add_subplot(111)

# Add first data column to ax1
ax1.bar(np.arange(len(data[:, 0])), data[:, 0], alpha=0.8, color='blue')
ax1.set_ylabel(data_labels[0], color='blue', fontsize=14)

# Add rest of data columns to new axes
axes = [ax1]
for i in range(1, len(data[0])):
    ax = axes[0].twinx()
    if plot_types[i] == 'line':
        ax.plot(np.arange(len(data[:, i])), data[:, i], color=f'C{i+1}')
    elif plot_types[i] == 'area':
        ax.fill_between(line_labels, data[:, i], alpha=0.5,color=f'C{i+1}')
    ax.set_ylabel(data_labels[i], color=f'C{i+1}', fontsize=14)
    ax.yaxis.label.set_color(f'C{i+1}')
    ax.spines['right'].set_edgecolor(f'C{i+1}')
    ax.spines['right'].set_position(('outward', 60*(i-1)))
    axes.append(ax)

plt.title("Agriculture and Food Production Metrics: Yearly Analysis", fontsize=20)
plt.xticks(np.arange(len(data[:, 0])), line_labels, rotation=45)
ax1.legend([data_labels[0]], loc='upper left')
for i in range(1, len(data[0])):
    axes[i].legend([data_labels[i]], loc='upper right')

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/233_202312311051.png')
plt.clf()

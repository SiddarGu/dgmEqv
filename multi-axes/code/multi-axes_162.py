import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data = '''Wheat,730,3072,42,83
Maize,195,1155,59,54
Rice,250,1252,50,34
Barley,180,974,54,28
Oats,170,688,40,21
Rye,120,532,44,19
Potatoes,1000,2450,24,75
Tomatoes,720,2712,38,98
Peas,250,1125,45,27
Carrots,410,1539,38,55'''

lines = data.split("\n")
data_labels = ["Total Production (Thousands of Tonnes)", "Revenue (Millions of Dollars)", 
               "Average Price (Dollars per Tonne)", "Imports (Thousands of Tonnes)"]
line_labels = [line.split(",")[0] for line in lines]
data = np.array([list(map(float, line.split(",")[1:])) for line in lines])
print(line_labels, data, data_labels)

colors = ['r', 'g', 'b', 'm']
plt_types = ['bar', 'line', 'area', 'scatter']
fig = plt.figure(figsize=(24, 15))
ax1 = fig.add_subplot(111)
ax1.bar(np.arange(len(line_labels)), data[:,0], color=colors[0], alpha=0.6, width=0.1)
ax1.set_xlabel('Product')
ax1.set_ylabel(data_labels[0], color=colors[0])

axs = [ax1]
for i in range(1, len(data_labels)):
    axs.append(ax1.twinx())
    if plt_types[i] == 'bar':
        axs[-1].bar(np.arange(len(line_labels))+i*0.1, data[:,i], color=colors[i], alpha=0.6, width=0.1)
    elif plt_types[i] == 'line':
        axs[-1].plot(line_labels, data[:,i], color=colors[i])
    elif plt_types[i] == 'area':
        axs[-1].fill_between(line_labels, 0, data[:,i], color=colors[i], alpha=0.4)
    elif plt_types[i] == 'scatter':
        axs[-1].scatter(line_labels, data[:,i], color=colors[i])
    axs[-1].set_ylabel(data_labels[i], color = colors[i])
    axs[-1].tick_params(axis='y', colors=colors[i])
    axs[-1].yaxis.set_major_locator(ticker.AutoLocator())
    if i>=2: axs[-1].spines['right'].set_position(('outward', (i-1)*60))

plt.title("Comprehensive Analysis of Agricultural & Food Production Revenue and Import")
ax1.legend([data_labels[i] for i in range(len(data_labels))])

for ax in axs[1:]:
    ax.legend([ax.get_ylabel()], loc="upper right")

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/252_202312311051.png')
plt.show()
plt.close()

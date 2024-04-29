import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# data transformation
raw_data = '''Sociology,4300,85,12000,512
Philosophy,2100,90,18000,876
History,3000,88,15000,357
Literature,2500,81,12500,154
Anthropology,2700,89,14000,418
Linguistics,1500,86,14500,317
Archaeology,1600,87,16000,491
Religious Studies,1200,92,17000,284
Gender Studies,1800,84,15500,165
Communication Studies,4000,88,13500,512
Cultural Studies,1900,90,18000,561'''
data_labels = ['Number of Students', 'Graduation Rate (%)', 'Average Tuition Fee ($)', 'Number of Publications']
line_labels = [row.split(',')[0] for row in raw_data.split('\n')]
data = np.array([row.split(',')[1:] for row in raw_data.split('\n')], dtype = float)

# plotting
fig, ax1 = plt.subplots(figsize=(22,10))
ax_arr = [ax1]
for i in range(1,len(data_labels)):
    ax_arr.append(ax1.twinx())

ax1.bar(line_labels, data[:,0],color='b', alpha=0.7, label=data_labels[0])
ax_arr[1].plot(line_labels, data[:,1],color='g', label=data_labels[1])
ax_arr[2].scatter(line_labels, data[:,2],color='r', label=data_labels[2])
ax_arr[3].fill_between(line_labels, data[:,3],color='c', alpha=0.5, label=data_labels[3])

colors = ['b','g','r','c']

for i, ax in enumerate(ax_arr):
    ax.set_ylabel(data_labels[i], color=colors[i])
    ax.tick_params(axis='y', colors=colors[i])
    if i>1:
        ax.spines['right'].set_position(('outward', 60*(i-1)))
    ax.yaxis.set_major_locator(AutoLocator())
    ax.legend(loc='upper left', bbox_to_anchor=(0.1, 1-0.1*i))

fig.tight_layout()
ax1.set_title('Social Sciences and Humanities: Student Data, Graduation Rates, Tuition Fees, and Academic Output')
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/86_2023122292141.png')
plt.close()

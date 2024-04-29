import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# preprocess data
data_str = '2014,52500,45100,40600,37500 2015,59700,48200,42800,40400 2016,67500,50900,44500,41800 2017,70800,52300,46500,44000 2018,75300,54700,48800,48800 2019,81100,56700,50300,52800 2020,82800,58800,52800,53800'
da= [ i.split(',') for i in data_str.split()] 
line_labels = [row[0] for row in da]
data = np.array([row[1:] for row in da]).astype(float).T
data_labels = ['Number of Graduates in Computer Science', 'Number of Graduates in Electrical Engineering',
               'Number of Graduates in Mechanical Engineering', 'Number of Graduates in Civil Engineering']
colors = ['r', 'g', 'b', 'y']

fig = plt.figure(figsize=(24, 10))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[0], color=colors[0], label=data_labels[0])
ax1.set_ylabel(data_labels[0], color=colors[0])

ax_list = [ax1]
for i in range(1, len(data)):
    ax = ax1.twinx()
    rspine = ax.spines['right']
    rspine.set_position(('axes', 1 + 0.2 * i))
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    ax.yaxis.set_ticks_position('right')
    ax.spines['right'].set_visible(True)
    ax.plot(line_labels, data[i], color=colors[i], label=data_labels[i])
    ax.set_ylabel(data_labels[i], color=colors[i])
    ax.yaxis.set_major_locator(ticker.AutoLocator())
    ax_list.append(ax)

plt.grid()
plt.title('Graduation Trends in Key Areas of Science and Engineering')

# Legend
axes = [ax for ax in ax_list]
labels = [ax.get_label() for ax in axes]
plt.legend(axes, labels, loc='upper left', bbox_to_anchor=(-0.1, 1), fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/194_202312310150.png', format='png')
plt.clf()

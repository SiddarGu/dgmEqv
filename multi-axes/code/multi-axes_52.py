import matplotlib.pyplot as plt
import numpy as np

# Data transformation
data = '''Psychology,485,2460,1520,860
Sociology,324,1790,910,520
History,289,1280,720,360
Political Science,312,1580,890,510
Anthropology,205,960,520,270
Literature,421,1970,1080,620
Philosophy,263,1340,740,410
Communication,379,2050,1290,720
Education,496,2470,1620,910
Linguistics,287,1460,820,460'''
data = [i.split(',') for i in data.split('\n')]
data_labels = ['Number of Publications','Number of Citations','Number of Authors','Number of Collaborations']
line_labels = [i[0] for i in data]
data = np.array([[int(j) for j in i[1:]] for i in data])

# Creating the primary ax (bar chart)
fig = plt.figure(figsize=(30,20))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')

# Creating other axes
colors = ['r', 'g', 'y']
for i in range(1, len(data_labels)):
    ax = ax1.twinx()
    if i == 1:
        ax.plot(line_labels, data[:,i], color=colors[i-1], label=data_labels[i])
    elif i == 2:
        ax.scatter(line_labels, data[:,i], color=colors[i-1], label=data_labels[i])
    else:
        ax.fill_between(line_labels, data[:,i], color=colors[i-1], label=data_labels[i], alpha=0.5)
    
    ax.set_ylabel(data_labels[i], color=colors[i-1])
    ax.tick_params(axis='y', colors=colors[i-1])
    ax.spines['right'].set_position(('outward', (i-1)*60))

# Legends and grid
ax1.legend(loc='upper left')
ax.legend(loc='upper right')
plt.grid()

plt.title('Social Sciences and Humanities Research Output Analysis')

# To prevent the overlapping of the labels
fig.autofmt_xdate()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/306_202312311430.png')
plt.clf()

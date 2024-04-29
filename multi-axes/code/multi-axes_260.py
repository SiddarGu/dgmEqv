import matplotlib.pyplot as plt
import numpy as np

# Provided data
data_str = "Modern Art,18000,360000,300/n Abstract Art,25500,510000,350/n Renaissance Art,36500,730000,600/n Impressionist Art,29000,580000,450/n Contemporary Art,15000,300000,400/n Expressionist Art,22000,440000,430/n Surreal Art,12500,250000,300/n Pop Art,20000,400000,350/n Performance Art,13500,270000,120/n Street Art,17500,350000,200"
data_str = data_str.replace(","," ")
data_str = data_str.replace("/n","\n")
data = np.loadtxt(data_str.split("\n"),dtype=str)

# Splitting the data into three varaibles
line_labels = data[:,0]
data = data[:, 2:].astype(float)
data_labels = ["Total Attendance", "Revenue (in $)", "Artwork Exhibits"]

# Define plot types
plot_types = ['bar', 'line', 'scatter']

# Create the figure and the axes
fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(111)

colors = ['r', 'b', 'g']

for i, label in enumerate(data_labels):
    if i == 0:
        ax1.bar(line_labels, data[:,i], color=colors[i], label = label)
        ax1.set_ylabel(label, color=colors[i])
        ax1.tick_params(axis='y', labelcolor=colors[i])
    else:
        ax = ax1.twinx()
        if plot_types[i] == 'line':
            ax.plot(line_labels, data[:,i], color=colors[i], label = label)
        if plot_types[i] == 'scatter':
            ax.scatter(line_labels, data[:,i], color=colors[i], label = label)
        ax.set_ylabel(label, color=colors[i])
        ax.tick_params(axis='y', labelcolor=colors[i])

fig.tight_layout()
plt.title('Analyzing Attendance, Revenue and Exhibit Variety in Different Categories of Art')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/59_2023122292141.png')
plt.show()
plt.close(fig)

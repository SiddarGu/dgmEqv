import matplotlib.pyplot as plt
import numpy as np

# Data
data_str = """Sport,Revenue (Billion $),Fanbase (Million People),Athlete Salary (Million $),Public Interest (Score)
Football,48,400,20,9\n
Basketball,12,800,30,8\n
Soccer,28,2000,50,10\n
Cricket,5,2500,10,7\n
Tennis,6,500,15,8\n
Baseball,10,500,22,7\n
Golf,4,200,20,6"""
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
data_values = [line.split(',')[1:] for line in data_lines[1:] if line.strip()]
line_labels = [line.split(',')[0] for line in data_lines[1:] if line.strip()]
data = np.array([[float(el) for el in row] for row in data_values])

# Create figure and subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
for i in range(len(data)):
    line_label = line_labels[i] + ' ' + str(data[i, 2])
    ax.scatter(data[i, 0], data[i, 1], c=colors[i], s=600 + (data[i, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2])) * 4400,
               label=None)
    ax.scatter([], [], c=colors[i], s=20, label=line_label)

# Legend
ax.legend(title=data_labels[2], loc='upper left', borderaxespad=0.)

# Colorbar
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3])))
cbar = plt.colorbar(sm)
cbar.ax.set_title(data_labels[3])

# Labels
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Title
plt.suptitle('Bubble Chart Analysis of Revenue, Fanbase, and Public Interest in Different Sports and Entertainment Industries')

# Save and show
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/296_202312310045.png')
plt.clf()

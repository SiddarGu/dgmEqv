
import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Brand Awareness (Score)", "Quality of Food (Score)", "Customer Service (Score)", "Price Level (Score)", "Variety (Score)"]
line_labels = ["Fast Food", "Cafes", "Restaurants", "Diners", "Catering"]
data = np.array([[90, 85, 80, 75, 70], [80, 85, 90, 95, 95], [85, 90, 95, 90, 85], [70, 75, 80, 85, 90], [75, 80, 85, 90, 95]])

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=plt.cm.Set1(i), label=line_labels[i], linewidth=2, alpha=0.5)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_rmax(100)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.94, 0.95), labelspacing=0.3, fontsize=14)

ax.set_title("Food & Beverage Industry Performance - 2021", fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/50_202312262320.png')
plt.clf()
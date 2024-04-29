
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Q1","Q2","Q3","Q4"] 
line_labels = ["Education (%)","Social Development (%)","Human Rights (%)","Arts and Culture (%)","Economic Equality (%)"]
data = np.array([[85,90,95,100], [70,75,80,85], [80,85,90,95], [65,70,75,80], [60,65,70,75]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)
for i in range(data.shape[0]):
    ax.plot(angles, data[i], label=line_labels[i])
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_rlim(0,100)
ax.set_title("Social and Human Development - 2023", fontsize=20)
legend = ax.legend(line_labels, loc='lower right', bbox_to_anchor=(1.4, 0.2), fontsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/27_202312262320.png')
plt.clf()

import numpy as np
import matplotlib.pyplot as plt

data_labels=["Production Volume (Unit/hour)", "Quality Control (Score)", "Maintenance (Score)", "Employee Efficiency (Score)", "Cost Management (Score)"]
data = np.array([[100,200,300,400,500],
                 [90,95,90,95,100],
                 [75,80,85,90,95],
                 [85,90,95,100,105],
                 [70,65,60,55,60]])
line_labels=["Factory A","Factory B","Factory C","Factory D","Factory E"]

angles=np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_ylim(0,600)
ax.set_title("Manufacturing and Production Performance Analysis", fontsize=20, pad=20)

for i in range(len(data)):
    ax.plot(angles, data[i], linewidth=3, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.3)
    ax.set_rlabel_position(0)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc='upper right', fontsize='x-large', bbox_to_anchor=(1.1, 1.1))

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/30_202312262320.png")
plt.clf()

import numpy as np
import matplotlib.pyplot as plt
data_labels=["Popularity (%)", "Variety (%)", "Quality (%)", "Impact (%)", "Accessibility (%)"]
line_labels=["Painting", "Theatre", "Musical Instruments", "Sculpture", "Dance"]
data=np.array([[70, 65, 60, 55, 50], [60, 65, 70, 75, 80], [80, 85, 90, 95, 100], [60, 65, 70, 75, 80], [75, 80, 85, 90, 95]])
data=np.concatenate((data, data[:, 0:1]), axis=1)
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, polar=True)
angles=np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
for i in range(len(data)):
    ax.plot(angles,data[i], color='C'+str(i), linewidth=1.5, label=line_labels[i])
    ax.fill(angles, data[i], color='C'+str(i), alpha=0.1)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_ylim(0,100) 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9, 0.95), fontsize=10)
ax.set_title('Arts and Culture Platform Performance in 2021', fontsize=18, fontweight='bold', y=1.08)
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/8_202312262320.png')
plt.clf()
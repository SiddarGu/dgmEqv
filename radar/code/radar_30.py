
import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Donations (%)", "Volunteering (%)", "Fundraising (%)", "Grants (%)", "Public Awareness (%)"]
line_labels = ["Red Cross", "UNICEF", "World Vision", "Oxfam", "Greenpeace"]
data = np.array([[90, 80, 75, 65, 60], [95, 90, 85, 80, 75], [80, 70, 65, 60, 55], [85, 75, 70, 65, 60], [90, 85, 80, 75, 70]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

ax.plot(angles, data[0], 'o-', c='#1f77b4', label=line_labels[0])
ax.plot(angles, data[1], 'o-', c='#ff7f0e', label=line_labels[1])
ax.plot(angles, data[2], 'o-', c='#2ca02c', label=line_labels[2])
ax.plot(angles, data[3], 'o-', c='#d62728', label=line_labels[3])
ax.plot(angles, data[4], 'o-', c='#9467bd', label=line_labels[4])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, 100)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower left', bbox_to_anchor=(-0.1, -0.4), ncol=3)

ax.yaxis.grid(True)

plt.title("Nonprofit and Charity Performance Evaluation")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/33_202312262320.png")
plt.clf()
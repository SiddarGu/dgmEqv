import matplotlib.pyplot as plt
import numpy as np

raw_data = "Domain,Web A,Web B,Web C,Web D\nSite Traffic,75,80,70,85\nUser Engagement,80,85,90,75\nContent Quality,70,65,75,80\nSite Navigation,90,85,80,95\nSecurity,85,80,95,90"
data_ = [row.split(',') for row in raw_data.split('\n')]

data_labels = data_[0][1:]
data = np.array([list(map(int, row[1:])) for row in data_[1:]])
line_labels = [row[0] for row in data_[1:]]

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, [0]]), axis=1)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

for i, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[i])
    radii = np.full_like(angles, (i+1) * data.max() / len(data))
    ax.plot(angles, radii, color='grey', ls='--', lw=0.5)
    ax.fill(angles, row, alpha=0.1)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlim(0, data.max())
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

ax.set_title('Website Performance Analysis in Technology and the Internet Sector', size=20, color='black', y=1.1)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/145_2023122292141.png')
plt.clf()

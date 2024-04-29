import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Fundraising Efforts (Million $)', 'Community Outreach (Score)', 
               'Program Expenses (Million $)', 'Administrative Costs (Million $)', 
               'Public Support (%)']
line_labels = ['Nonprofit A', 'Nonprofit B', 'Nonprofit C', 'Nonprofit D']
data = np.array([[58, 85, 50, 15, 70], 
                 [60, 80, 55, 18, 75], 
                 [62, 75, 52, 17, 77], 
                 [65, 90, 56, 16, 72]])

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
for i, row in enumerate(data):
    row_extended = np.concatenate((row, [row[0]]))
    ax.plot(angles, row_extended, label=line_labels[i])
    radius = np.full_like(angles, (i+1) * np.max(data) / len(data))
    ax.plot(angles, radius, color='grey')

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, rotation=45)
ax.set_rlim(0, np.max(data)*1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

plt.title('Charity and Nonprofit Organizations Performance Analysis')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/181_2023122292141.png', dpi=300)
plt.clf()


import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Funding (%)', 'Volunteers (Number)', 'Public Image (Score)', 'Number of Beneficiaries (Number)', 'Impact (Score)']
line_labels = ['Educational Organization', 'Environmental Organization', 'Animal Rescue', 'Social Services', 'Religious Organization']
data = np.array([[50, 60, 70, 80, 90], [100, 200, 300, 400, 500], [70, 75, 80, 85, 90], [50, 100, 150, 200, 250], [60, 65, 70, 75, 80]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=15)
ax.set_rlim([0, np.max(data) * 1.1])
ax.set_title('Nonprofit Performance Analysis - 2021',fontsize=20)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], 'o-', linewidth=2, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
plt.grid(color='gray', linestyle='--', linewidth=1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/35_202312262320.png') 
plt.clf()
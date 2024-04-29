
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Room occupancy rate (%)', 'Customer satisfaction (Score)', 
               'Service quality (Score)', 'Facility quality (Score)', 'Pricing (Score)']
line_labels = ['Beach hotel', 'City hotel', 'Hotel chain', 'Luxury hotel', 'Boutique hotel']
data = np.array([[80, 85, 90, 95, 90],
                 [85, 80, 75, 70, 65],
                 [90, 85, 80, 75, 70],
                 [75, 80, 85, 90, 95],
                 [70, 65, 60, 55, 60]])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_ylim(0, 100)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], 'o-', linewidth=2, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)

ax.set_title('Tourism and Hospitality Performance Evaluation', fontsize=18)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
ax.grid(linestyle='--', linewidth=2, alpha=0.5)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/42_202312262320.png')
plt.clf()
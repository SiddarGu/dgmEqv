
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ["Cost (Dollars)", "Patients Covered", "Average Premiums", "Insurers"]
line_labels = ["Private Health Insurance","Outpatient Care","Inpatient Care","Mental Health Care","Dental Care","Vision Care","Prescription Drugs"]
data = np.array([[98800,9502,3760,6], [70000,8502,4500,4], [80000,6200,3500,5], [60000,4200,4000,7], [54000,3000,3000,9], [18000,1500,2500,3], [20000,5000,2600,4]])

plot_types = ["bar chart", "line chart", "scatter chart", "area chart"]

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:,0], color = "#4D6AEE", label=data_labels[0])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], marker='o', color = "#A9C2F2", label=data_labels[1])


ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.scatter(line_labels, data[:,2], marker='*', color = "#F3C9F1", label=data_labels[2])

ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.2))
ax4.set_frame_on(True)
ax4.patch.set_visible(False)
ax4.plot(line_labels, data[:,3], color = "#F2A7F7", label=data_labels[3])

ax1.set_xlabel('Category')
ax1.set_ylabel('Cost (Dollars)')
ax2.set_ylabel('Patients Covered')
ax3.set_ylabel('Average Premiums')
ax4.set_ylabel('Insurers')

ax1.set_title('Healthcare and Health Analysis: Cost, Coverage, and Premiums')
ax1.grid(True)
ax1.legend(loc=1)
ax2.legend(loc=2)
ax3.legend(loc=3)
ax4.legend(loc=4)

plt.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/40_2023122270030.png')
plt.close('all')
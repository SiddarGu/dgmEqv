

import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Patients Treated (Thousands)", "Average Treatment Cost (Dollars)", "Average Time Spent in Treatment (Minutes)"]
line_labels = ["Primary Care", "Emergency Care", "Physical Therapy", "Mental Health Services", "Diagnostic Services", 
               "Surgical Services", "Radiology Services", "Dental Care", "Psychotherapy", "Rehabilitation"]
data = np.array([[1790, 220, 30], [1150, 400, 70], [1390, 220, 90], [600, 200, 60], [1340, 150, 45], [1620, 500, 120], 
                 [990, 300, 90], [900, 100, 60], [800, 150, 90], [1000, 200, 80]])

#Plot the data with the type of multi-axes chart
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], width=0.2, color='#00A0A0', alpha=0.6)
ax1.set_ylabel(data_labels[0], color='#00A0A0')
ax1.tick_params(axis='y', labelcolor='#00A0A0')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], '#FA5858', marker='o', linestyle='--', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='#FA5858')
ax2.tick_params(axis='y', labelcolor='#FA5858')

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], '#F5A9BC', marker='*', label=data_labels[2], linestyle=':')
ax3.set_ylabel(data_labels[2], color='#F5A9BC')
ax3.tick_params(axis='y', labelcolor='#F5A9BC')
ax3.spines['right'].set_position(('outward', 60))

plt.title('Healthcare Performance: Patient Treatment and Cost Analysis')
ax1.legend(data_labels[0], loc='upper left', bbox_to_anchor=(0.08, 1))
ax2.legend(data_labels[1], loc='upper center', bbox_to_anchor=(0.5, 1))
ax3.legend(data_labels[2], loc='upper right', bbox_to_anchor=(0.92, 1))
ax1.grid(True)
ax1.autoscale(tight=True)
ax2.autoscale(tight=True)
ax3.autoscale(tight=True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/21_2023122270030.png')
plt.clf()
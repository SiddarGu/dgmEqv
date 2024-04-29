
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Average Treatment Cost (Dollars)','Average Length of Stay (Days)','Patient Satisfaction Rate']
line_labels = ['Emergency Care', 'Outpatient Care', 'Inpatient Care', 'Diagnostic Services', 'Primary Care', 'Mental Health Services', 'Specialty Care', 'Rehabilitation Services', 'Home Health Services']
data = np.array([[45888, 15000, 3.2, 90], [12000, 6000, 1.5, 87], [35000, 20000, 10, 80], 
[18000, 1000, 0.5, 92], [13000, 3500, 2.5, 84], [4500, 15000, 4, 88], [10000, 8000, 5, 85], 
[6000, 10000, 7, 81], [3000, 4500, 2, 90]])

fig = plt.figure(figsize=(30, 15))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='#0b2267', width=0.3, alpha=0.8)
ax1.set_xlabel('Category', fontsize=20)
ax1.set_ylabel('Number of Patients Treated', fontsize=20, color='#0b2267')
ax1.tick_params(axis='y', labelcolor='#0b2267')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], '-o', color='#00776b', ms=14, label='Average Treatment Cost (Dollars)')
ax2.set_ylabel('Average Treatment Cost (Dollars)', fontsize=20, color='#00776b')
ax2.tick_params(axis='y', labelcolor='#00776b')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.05))
ax3.plot(line_labels, data[:,2], '-s', color='#f34b00', ms=14, label='Average Length of Stay (Days)')
ax3.set_ylabel('Average Length of Stay (Days)', fontsize=20, color='#f34b00')
ax3.tick_params(axis='y', labelcolor='#f34b00')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('axes', 1.1))
ax4.plot(line_labels, data[:,3], '-^', color='#f9a826', ms=14, label='Patient Satisfaction Rate')
ax4.set_ylabel('Patient Satisfaction Rate', fontsize=20, color='#f9a826')
ax4.tick_params(axis='y', labelcolor='#f9a826')

ax1.set_title('Healthcare and Health Performance Analysis: Number of Patients Treated, Cost, and Length of Stay', fontsize=25)
ax1.legend(loc='upper left', fontsize=20)
ax2.legend(loc='upper right', fontsize=20)
ax3.legend(loc='lower left', fontsize=20)
ax4.legend(loc='lower right', fontsize=20)

for ax in [ax1, ax2, ax3, ax4]:
    ax.tick_params(labelsize=18)
    
plt.autoscale()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/28_2023122270030.png')
plt.clf()
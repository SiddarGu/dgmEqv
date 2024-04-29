import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
raw_data = "Month,Number of Patients,Healthcare Spending (in 1000s),Prescriptions Filled\n January,1202,4500,3402\n February,1394,4800,3685\n March,1453,5100,3874\n April,1573,5200,4056\n May,1453,5300,3765\n June,1602,5200,3890\n July,1500,4700,3775\n August,1634,5000,3950\n September,1452,4800,3624\n October,1573,5000,3738\n November,1490,5200,3769\n December,1605,5300,3930"
lines = raw_data.split("\n")
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(int, line.split(',')[1:])) for line in lines[1:]])

# Figure initialization
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)

# Bar chart
ax1.bar(line_labels, data[:, 0], width=0.5, color='blue', alpha=0.75)
ax1.set_xlabel('Month')
ax1.set_ylabel(data_labels[0])
ax1.grid()

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='red')
ax2.set_ylabel(data_labels[1])

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 80))
ax3.fill_between(line_labels, 0, data[:, 2], color='green', alpha=0.5)
ax3.set_ylabel(data_labels[2])

ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='center left')
ax3.legend([data_labels[2]], loc='lower left')

plt.tight_layout()
plt.title('Monthly Trends in Healthcare: Patients, Spending, and Prescriptions Filled')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/179_202312310150.png')
plt.clf()

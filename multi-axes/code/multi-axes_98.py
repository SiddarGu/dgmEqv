import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Number of Patients", "Treatment Cost (Millions of Dollars)", "Average Length of Stay (Days)", "Number of Doctors Available"]
line_labels = ["Cardiology","Orthopedics","Pediatrics","Dermatology","Neurology","Ophthalmology","Psychiatry","Gynecology","Urology","Oncology"]

# Populate data
data = np.array([[800,10,5,20],[500,8,4,15],[600,9,3,12],[400,6,2,10],[700,12,6,18],
                 [900,15,7,25],[300,5,2,10],[400,7,3,15],[600,10,4,20],[1000,20,10,30]])

fig = plt.figure(figsize=(20,8))

# Add subplot and create initial bar plot
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='blue', alpha=0.5, label=data_labels[0])
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('blue')

# Overlay scatter plot, sharing the x-axis
ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:,1], color='red', label=data_labels[1])
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('red')

# Overlay line plot, sharing the x-axis
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], color='green', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2])
ax3.yaxis.label.set_color('green')

fig.autofmt_xdate()  # rotate x-axis labels for better readability

# Title and legends
plt.title("Healthcare Analysis: Patient Volume, Treatment Cost, and Service Availability", y=1.02)
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/338_202312311430.png")
plt.clf()  # clear figure for re-use

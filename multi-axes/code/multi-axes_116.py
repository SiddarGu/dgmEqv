import matplotlib.pyplot as plt
import numpy as np

# Parsing the provided data
data_str = "Category,Number of Patients,Treatment Cost (Millions of Dollars),Average Waiting Time (Minutes)/n General Medicine,5000,15,30/n Pediatrics,2500,12,25/n Surgery,3000,20,45/n Obstetrics and Gynecology,2000,18,40/n Orthopedics,3500,25,35/n Cardiology,4000,30,50/n Dermatology,1500,10,20/n Psychiatry,3000,22,55/n Dentistry,2500,8,15"
data_parts = data_str.split("/n")
labels = data_parts[0].split(',')
data = [item.split(',')[1:] for item in data_parts[1:]]
data = np.array(data, dtype=int)
line_labels = [item.split(',')[0] for item in data_parts[1:]]

fig = plt.figure(figsize=(30,20))
ax1 = fig.add_subplot(111)
width = 0.3
colors = ['b', 'r', 'g']

# Plotting the data
for i in range(data.shape[1]):
    if i==0:
        ax1.bar(np.arange(data.shape[0])-width/2, data[:, i], width=width, color=colors[i], alpha=0.6)
        ax1.set_ylabel(labels[i+1], color=colors[i])
        ax1.set_xticks(np.arange(data.shape[0]))
        ax1.set_xticklabels(line_labels, rotation=90)
        ax1.autoscale(axis='y')   
    else:
        ax = ax1.twinx()
        ax.plot(line_labels, data[:, i], '-o', color=colors[i])
        ax.set_ylabel(labels[i+1], color=colors[i])
        ax.spines['right'].set_position(('outward', 60*(i-1)))
        ax.autoscale(axis='y')
        ax.grid(False)

# Formatting and saving the figure
plt.title('Healthcare Facility Performance Analysis: Patient Volume, Cost, and Wait Times')
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/324_202312311430.png', dpi=300)
plt.close(fig)

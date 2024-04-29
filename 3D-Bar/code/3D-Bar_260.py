import matplotlib.pyplot as plt
import numpy as np

# Define data
data_str = 'Year,Criminal Cases Reported,Civil Lawsuits Filed,Legal Services Requests/n 2018,5000,2500,3000/n 2019,4700,2600,3150/n 2020,4900,2720,3200/n 2021,5000,2800,3500/n 2022,5100,2920,3700'
data_str = data_str.replace('/n', '\n')
data_list = [i.split(',') for i in data_str.split('\n')]

x_values = [i[0] for i in data_list[1:]]
y_values = data_list[0][1:]
data = np.array([i[1:] for i in data_list[1:]], dtype=np.float32)

# Create figure and 3D-axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot bars
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.4, 0.6, data[:, i], color=plt.cm.viridis(i/len(y_values)), alpha=0.8)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')
ax.view_init(elev=25, azim=165)

ax.set_title("Law and Legal Affairs: Case Reports and Service Requests Over Years", pad=20)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/252_202312310050.png')
plt.cla()


import numpy as np
import matplotlib.pyplot as plt

# Data Processing
data = "Discipline,Graduate Students,Undergraduate Students,Job Placement Rate (%)/n Physics,900,800,900/n Computer Engineering,350,1100,950/n Mechanical Engineering,300,1200,920/n Electrical Engineering,900,870,870/n Civil Engineering,250,960,890"
data = data.replace("/n", "\n").split("\n")
y_values = data[0].split(",")[1:]
x_values = [x.split(",")[0] for x in data[1:]]
numerical_data = np.array([list(map(int, x.split(",")[1:])) for x in data[1:]])

# Plotting
fig = plt.figure(figsize=[12, 8])  # Or other size based on actual data
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             np.ones(len(x_values)), np.ones(len(x_values)), numerical_data[:, i], 
             color=np.random.rand(3,), alpha=0.8)  

# Labels & Viewing Angle
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')
plt.title('Student Enrollment and Job Placement Rate in Science and Engineering disciplines', fontsize=12)
ax.set_ylabel('Metrics')
ax.set_xlabel('Discipline')

plt.tight_layout()
ax.view_init(elev=30, azim=-45) # Adjust the viewing angle
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/188_202312302235.png', format='png')
plt.clf()


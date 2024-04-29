import matplotlib.pyplot as plt
import numpy as np

# Raw data
raw_data = """Year,Theatre Attendance (Million),Museum Visits (Million),Music Concert Tickets Sold (Million),Art Exhibition Attendance (Million)
2015,2.5,3.2,4.2,4.5
2016,2.7,3.5,4.0,5.0
2017,2.9,3.8,4.5,5.2
2018,3.1,4.0,4.9,5.4
2019,3.3,4.2,5.2,5.6"""

# Process raw data
lines = raw_data.split("\n")
header = lines.pop(0).split(',')
data = np.array([line.split(',')[1:] for line in lines] , dtype=np.float32)
x_values = [line.split(',')[0] for line in lines]
y_values = header[1:]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
for i, y_value in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.4, 0.8, data[:,i], alpha=0.8, color=colors[i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=20, ha='right')
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Participation in Cultural Activities 2015-2019')
ax.set_xlabel('Year')
ax.grid()

# Adjust the viewing angles for better visualization
ax.view_init(elev=20, azim=-35)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/275_202312310050.png')  # Save the figure
plt.clf()  # Clear the current figure

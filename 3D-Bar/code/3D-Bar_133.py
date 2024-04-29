
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Theatre Attendance (Millions)', 'Cinema Attendance (Millions)', 'Museum Visits (Millions)', 'Music Concerts Attendance (Millions)']
data = np.array([[2.3, 1.4, 3.2, 1.5], [1.2, 1.5, 2.4, 3.2], [4.2, 3.1, 1.6, 4.5], [2.6, 2.7, 1.8, 2.4]])
x_values = ['Classical', 'Jazz', 'Rock', 'Pop']
    
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, [0]*len(x_values), 0.9, 0.9, data[:,i], alpha=0.5, color=['r','g','b','y'])
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticklabels(y_values)
ax.set_title('Arts and Culture Participation Analysis - Theatre, Cinema, Museum and Music Concerts')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/29_202312270030.png')
plt.clf()
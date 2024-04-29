
import numpy as np
import matplotlib.pyplot as plt

y_values=['Number of Scientists', 'Number of Engineers', 'Number of Graduates']
x_values=['Physics', 'Chemistry', 'Biology', 'Mathematics', 'Computer Science']
data=np.array([[200,400,1000],[175,325,875],[150,300,750],[125,275,625],[100,250,500]]).T

fig = plt.figure(figsize=(7,6)) 
ax = fig.add_subplot(111, projection='3d') 

x_data, y_data = np.meshgrid(np.arange(len(x_values)), np.arange(len(y_values))) 
x_data = x_data.flatten() 
y_data = y_data.flatten() 
z_data = data.flatten() 

ax.bar3d(x_data, y_data, np.zeros(len(z_data)), 1, 1, z_data, shade=True, alpha=0.9) 

ax.set_xticks(np.arange(len(x_values))) 
ax.set_xticklabels(x_values,rotation=20) 
ax.set_yticks(np.arange(len(y_values))) 
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Science and Engineering Workforce Trends')

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/19.png')
plt.show()
plt.clf()
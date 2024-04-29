
import matplotlib.pyplot as plt 
import numpy as np 

y_values = ['Average Math Score', 'Average Reading Score', 'Average Writing Score']
x_values = ['Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7'] 
data = np.array([[80, 90, 85], [85, 95, 90], [90, 100, 95], [95, 105, 100], [105, 110, 105]])

fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot(111, projection='3d') 

for i in range(len(y_values)): 
    xs = np.arange(len(x_values)) 
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(xs)), 0.8, 0.5, data[:, i], color='b', alpha=0.7) 

ax.set_xlabel('Grade Level') 
ax.set_xticks(np.arange(len(x_values))) 
ax.set_xticklabels(x_values, rotation=45)
ax.set_ylabel('Scores') 
ax.set_yticks(np.arange(len(y_values))) 
ax.set_yticklabels(y_values, rotation=-15, ha='left')

plt.title('Academic Performance by Grade Level - Average Scores')
plt.tight_layout() 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/22.png') 
plt.clf()
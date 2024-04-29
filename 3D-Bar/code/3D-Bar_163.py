
import numpy as np
import matplotlib.pyplot as plt

# Transform the data
y_values=['Literature (Books Published)','History (Publications)','Philosophy (Publications)','Sociology (Publications)']
x_values=['2010-2015','2016-2021','2022-2027']
data=np.array([[25,30,20,15],[35,40,30,20],[45,50,40,30]])

# Plotting the 3D bar chart
fig=plt.figure(figsize=(10,7))
ax=fig.add_subplot(111,projection='3d')

for i,y in enumerate(y_values):
    xs=np.arange(len(x_values))
    ys=[i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(xs)), 1, 1, data[:,i],alpha=0.4,color=plt.cm.Set1(i/len(y_values)))

# Setting the figure
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values,rotation=30, fontsize=18)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, fontsize=18)
ax.set_zlabel('Publications', fontsize=18)
ax.set_title('Publications in the Social Sciences and Humanities - 2010 to 2027', fontsize=20)

# Resize the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/49_202312270030.png')
plt.clf()
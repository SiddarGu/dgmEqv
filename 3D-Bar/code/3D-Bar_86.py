
import matplotlib.pyplot as plt
import numpy as np

y_values=['Number of Art Galleries','Number of Exhibitions','Number of Art Collectors']
x_values=['Painting','Sculpture','Photography','Mixed Media']
data=np.array([[30,70,100],[25,60,85],[20,50,85],[15,40,75]])

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111,projection='3d')

for i in range(len(y_values)):
    xs=np.arange(len(x_values))
    ys=[i]*len(x_values)
    ax.bar3d(xs,ys,np.zeros(len(x_values)),1,1,data[:,i],shade=True,alpha=0.5, color='r')

ax.set_yticks(np.arange(len(y_values)))
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values,rotation=45)
ax.set_yticklabels(y_values)
ax.set_title('Arts and Culture Activity Overview')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/32_202312270030.png')
plt.clf()
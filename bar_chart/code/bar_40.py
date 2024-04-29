
import matplotlib.pyplot as plt
import numpy as np

data= np.array([[240,180,150],
                [60,50,40],
                [90,70,60],
                [80,60,50]])

x_labels= ['USA','UK','Germany','France']
y_labels= ['Facebook Users(million)','Instagram Users(million)','Twitter Users(million)']

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
width = 0.2
x_pos = np.arange(len(x_labels))

for i in range(3):
    ax.bar(x_pos+(i-1)*width,data[:,i],width,label=y_labels[i])

ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels,rotation=45,ha='right',wrap=True)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3,fancybox=True,shadow=True)
ax.set_title('Number of Social Media Users in four countries in 2021')
fig.tight_layout()

plt.savefig('bar chart/png/531.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

data = np.array([[250,500],[200,400],[180,320],[210,480]])

xlabels = ['USA','UK','Germany','France']

fig, ax = plt.subplots(figsize=(8,4))

ax.bar(xlabels,data[:,0], width=0.4, label='Internet Users(million)', color='#006699')
ax.bar(xlabels,data[:,1], bottom=data[:,0], width=0.4, label='Data Usage(GB)', color='#3399cc')

ax.set_title('Internet users and data usage in four countries in 2021')
ax.set_ylabel('Number')
ax.set_xlabel('Country')

ax.legend(loc='best')
ax.grid(True, linestyle='-', color='#cccccc', linewidth=1)

for i in range(len(data)):
    ax.annotate(data[i], xy=(xlabels[i],data[i][0]/2+data[i][1]/2+0.3), ha='center', va='center')

plt.xticks(xlabels)

plt.tight_layout()
plt.savefig('Bar Chart/png/246.png')
plt.clf()
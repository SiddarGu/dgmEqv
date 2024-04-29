
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

data = np.array([[2001,500,800,400],
                 [2002,600,900,500],
                 [2003,700,1000,600],
                 [2004,800,1100,700],
                 [2005,900,1200,800]])

plt.plot(data[:,0],data[:,1], label='Wheat Production (million tons)', marker='o')
plt.plot(data[:,0],data[:,2], label='Corn Production (million tons)', marker='o')
plt.plot(data[:,0],data[:,3], label='Barley Production (million tons)', marker='o')

plt.xticks(data[:,0])
plt.title('Global Grain Production from 2001 to 2005')
plt.xlabel('Year')
plt.ylabel('Production (million tons)')
plt.legend(loc='best', bbox_to_anchor=(1.0, 0.5))

for i in range(len(data)):
    ax.annotate(data[i,1], xy=(data[i,0],data[i,1]),  xytext=(data[i,0] + 0.2,data[i,1] + 20))
    ax.annotate(data[i,2], xy=(data[i,0],data[i,2]),  xytext=(data[i,0] + 0.2,data[i,2] + 20))
    ax.annotate(data[i,3], xy=(data[i,0],data[i,3]),  xytext=(data[i,0] + 0.2,data[i,3] + 20))

plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/157.png')
plt.clf()
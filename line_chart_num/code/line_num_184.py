
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

data = np.array([[2001,20,4,2],
                 [2002,22,3,3],
                 [2003,25,2,4],
                 [2004,27,1,3]])

x = data[:,0]
y1 = data[:,1]
y2 = data[:,2]
y3 = data[:,3]

ax.plot(x, y1, color='red', linestyle='-', marker='o', label='GDP(billion dollars)')
ax.plot(x, y2, color='green', linestyle='-', marker='o', label='Unemployment Rate(%)')
ax.plot(x, y3, color='blue', linestyle='-', marker='o', label='Inflation Rate(%)')

ax.legend(loc='upper center')
ax.set_title('Economic Performance of the United States in 2001-2004')

for i in range(len(x)):
    ax.annotate(str(y1[i]), xy=(x[i],y1[i]), xytext=(x[i]-0.2,y1[i]+0.3))
    ax.annotate(str(y2[i]), xy=(x[i],y2[i]), xytext=(x[i]-0.2,y2[i]+0.3))
    ax.annotate(str(y3[i]), xy=(x[i],y3[i]), xytext=(x[i]-0.2,y3[i]+0.3))

plt.xticks(x)
plt.tight_layout()
plt.savefig('line chart/png/508.png')
plt.clf()
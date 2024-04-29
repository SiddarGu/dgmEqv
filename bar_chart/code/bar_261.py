
import matplotlib.pyplot as plt
import numpy as np

data=[[2010,800,500],[2011,900,600],[2012,1000,700],[2013,1100,800]]

fig=plt.figure(figsize=(8,4))
ax=fig.add_subplot(111)

x_pos = np.arange(4)

ax.bar(x_pos-0.2, [point[1] for point in data],width=0.4,label='Internet Users',align='edge')
ax.bar(x_pos+0.2, [point[2] for point in data],width=0.4,label='Smartphone Users',align='edge')

ax.set_xticks(x_pos)
ax.set_xticklabels([point[0] for point in data],rotation=45, fontsize=7, wrap=True)
ax.set_title('Growth of Internet and Smartphone Users from 2010 to 2013')
ax.legend(loc='upper left', fontsize=8)

plt.tight_layout()
plt.savefig('bar chart/png/258.png')
plt.clf()
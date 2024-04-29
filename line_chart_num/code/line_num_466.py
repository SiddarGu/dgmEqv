
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot()
ax.plot([0,1,2,3,4,5,6,7], [10,15,20,30,25,20,15,10], 
        color='blue', linestyle='dashed', marker='o',
        markerfacecolor='red', markersize=8)
ax.set_xticks([0,1,2,3,4,5,6,7])
ax.set_title("Data Transfer Rate of a Network on March 19, 2023")
ax.set_xlabel('Time')
ax.set_ylabel('Data Transfer Rate (Gbps)')
for a,b in zip([0,1,2,3,4,5,6,7], [10,15,20,30,25,20,15,10]):
    ax.annotate(str(b),xy=(a,b),xycoords='data')
plt.tight_layout()
plt.savefig('line chart/png/362.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

data = np.array([[200,400,600],[250,450,650],[210,470,620],[220,430,590]])

x = np.arange(4)
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

ax.bar(x,data[:,0],width=0.2,bottom=data[:,1]+data[:,2],label='Solar',color='orange')
ax.bar(x,data[:,1],width=0.2,bottom=data[:,2],label='Wind',color='green')
ax.bar(x,data[:,2],width=0.2,label='Hydro',color='blue')

plt.xticks(x,["East","West","North","South"])
plt.ylabel("Energy production (MWh)")
plt.title("Energy production from solar, wind, and hydro sources in four regions in 2021")
plt.legend(loc=2)
for x,y in enumerate(data):
    ax.text(x,y.sum()/2,y.sum(),ha="center",va="bottom",rotation=90)
plt.tight_layout()
plt.savefig("Bar Chart/png/470.png")
plt.clf()
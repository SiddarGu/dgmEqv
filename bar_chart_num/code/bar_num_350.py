
import matplotlib.pyplot as plt 
import numpy as np

data=np.array([[2019,12000,5000],[2020,14000,6000],[2021,16000,7000]])

plt.figure(figsize=(10,6)) 

ax=plt.subplot()
ax.bar(data[:,0],data[:,1],label="Research Papers Published",color='blue',bottom=data[:,2],width=0.5)
ax.bar(data[:,0],data[:,2],label="Books Published",color='red',width=0.5) 

ax.set_xticks(data[:,0])
ax.set_xticklabels(data[:,0])

for i,j in zip(data[:,0],data[:,1]):
    ax.annotate(str(j),xy=(i,j/2),ha="center")

for i,j in zip(data[:,0],data[:,2]):
    ax.annotate(str(j),xy=(i,j+j/2),ha="center")

plt.title("Number of research papers and books published in social sciences and humanities from 2019 to 2021")
ax.legend()
plt.tight_layout()
plt.savefig("Bar Chart/png/37.png")
plt.clf()
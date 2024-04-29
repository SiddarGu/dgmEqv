
import matplotlib.pyplot as plt
import numpy as np

data=np.array([[500,150,20],[400,170,25],[550,200,30],[450,190,35]])

x=np.arange(4)
country=['USA','UK','Germany','France']

plt.figure(figsize=(10,7))
ax=plt.subplot()
ax.bar(x-0.2,data[:,0],width=0.2,color='b',label='Studies')
ax.bar(x,data[:,1],width=0.2,color='r',label='Research Projects')
ax.bar(x+0.2,data[:,2],width=0.2,color='g',label='Grants')
plt.title('Social sciences and humanities studies, research projects and grants in four countries in 2021')
plt.xticks(x,country)
plt.legend()
for i in range(len(x)):
    plt.text(x[i],data[i,0],data[i,0],ha='center',va='bottom')
    plt.text(x[i],data[i,0]+data[i,1],data[i,1],ha='center',va='bottom')
    plt.text(x[i],data[i,0]+data[i,1]+data[i,2],data[i,2],ha='center',va='bottom')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('Bar Chart/png/221.png',dpi=300)
plt.clf()
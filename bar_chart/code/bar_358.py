
import matplotlib.pyplot as plt
import numpy as np

data= [['USA',170,60],['UK',130,40],['Germany',150,50],['France',140,45]]

label=[]
crops=[]
livestock=[]

for i in data:
    label.append(i[0])
    crops.append(i[1])
    livestock.append(i[2])

x=np.arange(len(label)) 
width=0.35

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot()
ax.bar(x,crops,width,label='Crops',color='orange')
ax.bar(x+width,livestock,width,label='Livestock',color='green')

ax.set_ylabel("Million Tons")
ax.set_title("Agricultural production of crops and livestock in four countries in 2021")
ax.set_xticks(x+width/2)
ax.set_xticklabels(label,rotation=45,ha="right",rotation_mode="anchor")
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig("bar chart/png/300.png")
plt.clf()
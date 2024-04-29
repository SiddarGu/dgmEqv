
import matplotlib.pyplot as plt
import numpy as np

Region = ["Asia","Europe","North America","South America"]
Athletes = [1000,800,900,700]
Viewers = [4500,4000,4550,4200]

fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot() 
ax.bar(Region,Athletes,width=0.2,bottom=0,color='r',label='Athletes') 
ax.bar(Region,Viewers,width=0.2,bottom=Athletes,color='g',label='Viewers') 
ax.set_title('Number of athletes and viewers in four regions in 2021')
ax.set_xlabel('Region')
ax.set_ylabel('Number')
ax.legend(loc='upper left')
plt.xticks(Region)
plt.tight_layout()
plt.savefig("bar chart/png/467.png")
plt.clf()
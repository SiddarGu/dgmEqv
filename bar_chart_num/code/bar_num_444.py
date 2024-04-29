
import matplotlib.pyplot as plt 
import numpy as np

Country = ['USA','UK','Germany','France']
Crops = [3000,4000,5000,6000]
Livestock = [20000,18000,17000,19000]

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot()
ax.bar(Country,Crops,bottom=Livestock,width=0.5,label='Crops')
ax.bar(Country,Livestock,width=0.5,label='Livestock')
plt.title('Agriculture and food production in four countries in 2021')

ax.set_xticks(Country)
ax.set_ylabel('Hectares/Heads')
ax.set_xlabel('Country')
ax.legend(loc = 'upper center')

for i in range(len(Country)):
    ax.annotate(str(Crops[i]+Livestock[i]),xy=(i-0.25,Crops[i]+Livestock[i]+1000),rotation = 45,horizontalalignment='center',verticalalignment='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/78.png')
plt.clf()
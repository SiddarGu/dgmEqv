
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(15,8))
ax=fig.add_subplot(111)

Country=['USA','UK','Germany','France']
Hospitals=[3000,1500,1200,2000]
Hospital_Beds=[2.2,1.3,1.1,1.7]
Doctors=[900,450,400,600]

p1=ax.bar(Country,Hospitals,bottom=0,label='Hospitals')
p2=ax.bar(Country,Hospital_Beds,bottom=Hospitals,label='Hospital Beds')
p3=ax.bar(Country,Doctors,bottom=np.array(Hospitals)+np.array(Hospital_Beds),label='Doctors')

ax.set_title('Number of hospitals, hospital beds, and doctors in four countries in 2021')
ax.legend(loc='upper left')
ax.set_xticks(Country)

for i in range(len(Hospitals)):
    ax.annotate(Hospitals[i],xy=(i,Hospitals[i]/2),ha='center')
    ax.annotate(Hospital_Beds[i],xy=(i,Hospitals[i]+Hospital_Beds[i]/2),ha='center')
    ax.annotate(Doctors[i],xy=(i,Hospitals[i]+Hospital_Beds[i]+Doctors[i]/2),ha='center',wrap=True)

plt.tight_layout()
plt.savefig('Bar Chart/png/354.png')
plt.clf()
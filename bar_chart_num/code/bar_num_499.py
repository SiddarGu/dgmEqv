
import matplotlib.pyplot as plt
import numpy as np

Region=['North America','Europe','Asia','South America']
Hospitals=[750,650,600,500]
Medical_Centers=[1000,900,1100,900]
Pharmacies=[3000,2500,2700,2200]

x=np.arange(len(Region))
width=0.2

fig,ax=plt.subplots(figsize=(8,6))

rects1=ax.bar(x-width,Hospitals,width=width,label='Hospitals')
rects2=ax.bar(x,Medical_Centers,width=width,label='Medical Centers')
rects3=ax.bar(x+width,Pharmacies,width=width,label='Pharmacies')

ax.set_title('Number of healthcare facilities in four regions in 2021')
ax.set_ylabel('Number')
ax.set_xlabel('Region')
ax.set_xticks(x)
ax.set_xticklabels(Region)
ax.legend()

for rect in rects1:
    height=rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x()+rect.get_width()/2,height),
                xytext=(0,3),
                textcoords='offset points',
                ha='center',
                va='bottom')

for rect in rects2:
    height=rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x()+rect.get_width()/2,height),
                xytext=(0,3),
                textcoords='offset points',
                ha='center',
                va='bottom')

for rect in rects3:
    height=rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x()+rect.get_width()/2,height),
                xytext=(0,3),
                textcoords='offset points',
                ha='center',
                va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/76.png')
plt.clf()
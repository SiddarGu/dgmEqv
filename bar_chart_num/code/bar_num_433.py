
import matplotlib.pyplot as plt
import numpy as np

#Set data
Country=['USA','UK','Germany','France']
Donations=[10,12,9,11]
Volunteers=[500,450,400,470]

#Set figure
fig, ax = plt.subplots(figsize=(7,7))

#Set title
ax.set_title('Donations and volunteers in four countries in 2021')

#Plot bar
bar1=ax.bar(Country,Donations,bottom=0,label='Donations(million)')
bar2=ax.bar(Country,Volunteers,bottom=Donations,label='Volunteers')

#Set xticks
ax.set_xticks(Country)

#Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

#Set annotation
for rect1,rect2 in zip(bar1,bar2):
    height1 = rect1.get_height()
    height2 = rect2.get_height()
    ax.annotate('{}'.format(height1),
                xy=(rect1.get_x() + rect1.get_width() / 2, height1),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate('{}'.format(height2),
                xy=(rect2.get_x() + rect2.get_width() / 2, height1+height2/2),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

#Set grid and tight layout
ax.grid()
plt.tight_layout()

#Save fig
plt.savefig('Bar Chart/png/32.png')

#Clear figure
plt.clf()
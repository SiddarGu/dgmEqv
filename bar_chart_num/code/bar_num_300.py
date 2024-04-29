
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(8,5))
ax=fig.add_subplot()

Country=np.array(['USA','UK','Germany','France'])
Sports_Teams=np.array([20,15,17,18])
Attendance=np.array([20000,18000,17500,19000])

p1=ax.bar(Country,Sports_Teams,label='Sports Teams')
p2=ax.bar(Country,Attendance,label='Attendance',bottom=Sports_Teams)

ax.set_title('Number of sports teams and attendance in four countries in 2021')
ax.set_xticks(Country)
ax.legend(loc='upper center')

for i,rect in enumerate(p1):
    ax.annotate(Sports_Teams[i],xy=(rect.get_x()+(rect.get_width()/2),rect.get_height()/2),
                xytext=(0,3),textcoords='offset points',
                ha='center',va='bottom')
for i,rect in enumerate(p2):
    ax.annotate(Attendance[i],xy=(rect.get_x()+(rect.get_width()/2),rect.get_height()+rect.get_y()+Sports_Teams[i]/2),
                xytext=(0,3),textcoords='offset points',
                ha='center',va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/224.png')
plt.clf()
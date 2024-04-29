
            
import matplotlib.pyplot as plt

data=[(2015,4,2.5),(2016,5,3),(2017,6,3.5),(2018,7,4),(2019,8,4.5),(2020,10,5)]

year=[i[0] for i in data]
smartphone=[i[1] for i in data]
internet=[i[2] for i in data]

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot()
ax.bar(year,smartphone,bottom=internet,width=0.5,align='center',label='Smartphone Users')
ax.bar(year,internet,width=0.5,align='center',label='Internet Users')
ax.set_xticks(year)
ax.legend()
ax.set_title('Smartphone and Internet users from 2015 to 2020')
for i,j in enumerate(smartphone):
    ax.annotate(int(j),xy=(year[i],smartphone[i]/2+internet[i]), fontsize=14, ha='center')
for i,j in enumerate(internet):
    ax.annotate(int(j),xy=(year[i],internet[i]/2), fontsize=14, ha='center')
plt.tight_layout()
plt.savefig('Bar Chart/png/300.png')
plt.clf()
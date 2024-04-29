
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()
Country = ['USA','UK','Germany','France']
Rate = [0.65,0.7,0.75,0.8]
Num = [300000,450000,520000,400000]

ax.bar(Country,Rate,label='Hotel Occupancy Rate')
ax.bar(Country,Num,bottom=Rate,label='Number of Tourists')

ax.set_title('Hotel occupancy rate and number of tourists in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Rate/Num')
ax.legend(loc='upper center')
ax.set_xticks(Country)

for x,y in zip(Country,Rate):
    ax.annotate('{:.2f}'.format(y),xy=(x,y+0.02))
for x,y in zip(Country,Num):
    ax.annotate('{:.0f}'.format(y),xy=(x,y+0.02))

plt.tight_layout()
plt.savefig('Bar Chart/png/291.png')
plt.clf()
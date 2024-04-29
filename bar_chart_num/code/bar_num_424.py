
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
Country = ['USA','UK','Germany','France']
Hotels = [10000,7000,9000,8000]
Restaurants = [8000,9000,7000,8000]
Tourists = [12000,11000,10000,9000]
x = range(len(Country))
ax.bar(x, Hotels, bottom=Restaurants, color='#f9a602', label='Hotels', width=0.3, align='center')
ax.bar(x, Restaurants, bottom=Tourists, color='#0072bc', label='Restaurants', width=0.3, align='center')
ax.bar(x, Tourists, color='#ed1c24', label='Tourists', width=0.3, align='center')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend(loc='upper left')
for i,j in zip(x,Hotels):
    ax.annotate(str(j),xy=(i-0.12,j/2+Restaurants[i]/2+Tourists[i]/2))
for i,j in zip(x,Restaurants):
    ax.annotate(str(j),xy=(i-0.12,j/2+Tourists[i]/2))
for i,j in zip(x,Tourists):
    ax.annotate(str(j),xy=(i-0.12,j/2))
plt.title('Number of hotels, restaurants and tourists in four countries in 2021')
plt.tight_layout()
plt.savefig('Bar Chart/png/162.png')
plt.clf()

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

year=['2011','2012','2013','2014','2015']
crim=[10000,11000,12000,13000,14000]
civil=[15000,14000,15000,14000,15000]
total=[25000,25000,27000,27000,29000]

plt.figure(figsize=(8,4))
ax=plt.subplot()
plt.plot(year,crim,label='Criminal Cases Filed',color='r')
plt.plot(year,civil,label='Civil Cases Filed',color='b')
plt.plot(year,total,label='Total Cases Filed',color='g')

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xticks(year)
plt.title("Cases Filed in U.S. Courts from 2011-2015")
plt.xlabel('Year')
plt.ylabel('Cases Filed')
plt.legend(loc=0)

for i,j in zip(year,total):
    ax.annotate(str(j),xy=(i,j))

plt.tight_layout()
plt.savefig('line chart/png/306.png')
plt.clf()
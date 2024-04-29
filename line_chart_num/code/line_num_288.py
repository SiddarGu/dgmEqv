
import matplotlib.pyplot as plt

year=[2001,2002,2003,2004,2005,2006,2007,2008]
hpi=[115,125,135,145,155,165,175,185]
hs=[1000,1200,1400,1600,1800,2000,2200,2400]

plt.figure(figsize=(10,4))
ax = plt.subplot() 

ax.plot(year,hpi,label='Housing Price Index',color='purple',marker='o')
ax.plot(year,hs,label='Number of Houses Sold',color='green',marker='o')
ax.set_title('Housing Price Index and Number of Houses Sold in the US from 2001-2008')
ax.set_xlabel('Year')
ax.set_ylabel('Index/Number of Houses Sold')
ax.legend(loc='upper right')
ax.tick_params(axis='x',rotation=45)

for i,j in zip(year,hpi):
    ax.annotate(str(j),xy=(i,j))
    
for i,j in zip(year,hs):
    ax.annotate(str(j),xy=(i,j))
    
plt.tight_layout()
plt.savefig('line chart/png/454.png')
plt.clf()
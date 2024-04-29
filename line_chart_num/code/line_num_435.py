
import matplotlib.pyplot as plt
from matplotlib import ticker

year=[2000,2001,2002,2003,2004]
tax=[25,28,30,33,35]
gdp=[12,15,18,20,25]

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot()
ax.plot(year,tax,label='Tax Rate',marker='o',linestyle='--',color='r',markersize=8)
ax.plot(year,gdp,label='GDP',marker='o',linestyle='-',color='b',markersize=8)

ax.set_title('Tax Rate and GDP in the United States from 2000 to 2004')

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_xlabel('Year')
ax.set_ylabel('Tax Rate (%)/GDP (trillion dollars)')
ax.legend(loc='upper left')

for a,b,c in zip(year,tax,gdp):
    ax.text(a-0.2,b+0.2,str(b)+'%',fontsize='12')
    ax.text(a-0.2,c-0.2,str(c),fontsize='12')

plt.tight_layout()
plt.savefig('line chart/png/535.png')
plt.clf()
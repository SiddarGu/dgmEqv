
import matplotlib.pyplot as plt
import numpy as np

x=np.array([2017,2018,2019,2020,2021,2022,2023])
tax_rate=[15,17,20,22,25,28,30]
employment_rate=[80,78,76,74,72,70,68]
gdp=[2.5,2.6,2.7,2.8,2.9,3.0,3.1]

fig=plt.figure(figsize=(15,6))
ax=fig.add_subplot(111)
ax.plot(x,tax_rate,label='Tax Rate (%)',color='red',marker='o',markerfacecolor='red',markersize=10)
ax.plot(x,employment_rate,label='Employment Rate (%)',color='green',marker='o',markerfacecolor='green',markersize=10)
ax.plot(x,gdp,label='GDP (trillion dollars)',color='blue',marker='o',markerfacecolor='blue',markersize=10)
ax.set_xlabel('Year')
ax.set_title('Changes in Tax Rate, Employment Rate and GDP in the US from 2017 to 2023',fontsize=15)
ax.legend(loc='lower right',fontsize=15)
ax.grid(True)

plt.xticks(x)
plt.tight_layout()
plt.savefig('line chart/png/422.png')
plt.clf()
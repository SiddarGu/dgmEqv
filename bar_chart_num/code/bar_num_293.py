
import numpy as np
import matplotlib.pyplot as plt

data= {'Country':['USA','UK','Germany','France'],
       'Coffee Consumption(kg/year)':[400,350,300,250],
       'Tea Consumption(kg/year)':[200,230,180,220]
      }

country=data['Country']
coffee_consumption=data['Coffee Consumption(kg/year)']
tea_consumption=data['Tea Consumption(kg/year)']

fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot(1,1,1)

ax.bar(country,coffee_consumption,width=0.3,bottom=tea_consumption,label='Coffee Consumption')
ax.bar(country,tea_consumption,width=0.3,label='Tea Consumption')

for i in range(len(country)):
    ax.text(x=i,y=coffee_consumption[i]+tea_consumption[i]/2,s=coffee_consumption[i]+tea_consumption[i],ha='center',va='center',rotation=45,wrap=True)

ax.set_title('Coffee and Tea Consumption in Four Countries in 2021')
ax.set_ylabel('Consumption(kg/year)')
ax.set_xticks(ticks=range(len(country)))
ax.set_xticklabels(labels=country)
ax.legend()

plt.tight_layout()
plt.savefig('Bar Chart/png/120.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Electricity_Consumption = [4000,3000,5000,3500]
Renewable_Energy = [13,30,45,20]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
x = np.arange(len(Country))
ax.bar(x-0.2,Electricity_Consumption,width=0.4,label='Electricity Consumption(TWh)', color='lightblue')
ax.bar(x+0.2,Renewable_Energy,width=0.4,label='Renewable Energy(% of total electricity)', color='lightgreen')

ax.set_title('Electricity Consumption and Renewable Energy in four countries in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5)
ax.set_xticks(x)
ax.set_xticklabels(Country,rotation=45, ha="right",fontsize=12)
ax.set_ylabel('Quantity')
plt.tight_layout()
plt.savefig('bar chart/png/487.png')
plt.clf()
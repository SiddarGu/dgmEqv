
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot()

labels=["Corporate Taxes","Individual Taxes", "Payroll Taxes", "Property Taxes", "Other"]
sizes=[25,45,15,10,5]
explode=[0.1,0,0,0,0]
colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#aaff80']

ax.pie(sizes,labels=labels,explode=explode,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
ax.axis('equal')
ax.set_title('Breakdown of Tax Revenue for the U.S. Government in 2023')
ax.legend(loc='lower right',bbox_to_anchor=(1.1,0.5))

plt.xticks(rotation=90, wrap=True)
fig.tight_layout()
plt.savefig('pie chart/png/425.png', bbox_inches='tight')
plt.clf()
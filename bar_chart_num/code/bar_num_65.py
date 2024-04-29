

import matplotlib.pyplot as plt
import numpy as np

data = {'Country':['USA','UK','Germany','France'],
        'Charitable Donations (million)':[2400,1800,2100,2300],
        'Nonprofit Organizations':[4500,4000,4700,4200]}

Country = data['Country']
Charitable_Donations = data['Charitable Donations (million)']
Nonprofit_Organizations = data['Nonprofit Organizations']

x = np.arange(len(Country))

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111)
ax.bar(x-0.2, Charitable_Donations, color='b', width=0.4, label='Charitable Donations (million)')
ax.bar(x+0.2, Nonprofit_Organizations, color='c', width=0.4, label='Nonprofit Organizations')

ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend(loc='best')
ax.set_title('Charitable Donations and Number of Nonprofit Organizations in four countries in 2021')

for i in range(len(Country)):
    ax.annotate('%d' %Charitable_Donations[i], xy=(x[i]-0.2,Charitable_Donations[i]+200))
    ax.annotate('%d' %Nonprofit_Organizations[i], xy=(x[i]+0.2,Nonprofit_Organizations[i]+200))

plt.tight_layout()
plt.savefig('Bar Chart/png/38.png')
plt.show()
plt.clf()


import matplotlib.pyplot as plt 
plt.figure(figsize=(10,5)) 
ax = plt.subplot()
ax.plot([2018,2019,2020,2021,2022],[180,200,220,220,240],color='crimson',label='Average Home Price(thousands of dollars)')
ax.plot([2018,2019,2020,2021,2022],[140,150,160,170,180],color='darkblue',label='Average Apartment Price(thousands of dollars)')
plt.title('Average Home and Apartment Prices in the United States from 2018 to 2022')
plt.xticks([2018,2019,2020,2021,2022])
plt.legend(loc='best', frameon=False,prop={'size': 10})
plt.tight_layout()
plt.savefig('line chart/png/196.png')
plt.clf()
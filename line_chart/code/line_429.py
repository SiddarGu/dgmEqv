

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

year = [2010,2011,2012,2013,2014]
donations = [3000,4000,3500,4500,5000]
volunteers = [20000,21000,19000,22000,24000]

ax.plot(year,donations,color='#00A0A0',label='Donations(million dollars)')
ax.plot(year,volunteers,color='#B20000',label='Volunteers')

plt.legend(loc='upper left')
plt.title('Increase of donations and volunteers in a non-profit organization from 2010 to 2014')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.xticks(year)

plt.tight_layout()
plt.savefig('line chart/png/319.png')
plt.clf()
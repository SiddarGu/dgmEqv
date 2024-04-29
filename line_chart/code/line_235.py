

import matplotlib.pyplot as plt

plt.figure(figsize=(9, 6))

plt.plot([2000,2004,2008,2012,2016,2020], [2.2,2.6,3.2,3.4,3.8,4.2], label = 'Number of immigrants(million)')
plt.plot([2000,2004,2008,2012,2016,2020], [280,310,350,380,420,460], label = 'Population(million)')

plt.title('Immigration and Population Changes in the United States from 2000-2020')
plt.xlabel('Year')
plt.ylabel('Number')
plt.xticks([2000,2004,2008,2012,2016,2020])
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/269.png')
plt.clf()
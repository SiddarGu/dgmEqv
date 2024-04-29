
import matplotlib.pyplot as plt
import numpy as np

data = [[2016,100,50,60,20],
        [2017,90,55,80,30],
        [2018,110,45,65,40],
        [2019,120,60,75,35]]

data = np.array(data)

plt.figure(figsize=(7,5))
plt.plot(data[:,0], data[:,1], color='red', linestyle='--', marker='o', label='Donations to Charity A')
plt.plot(data[:,0], data[:,2], color='green', linestyle='--', marker='^', label='Donations to Charity B')
plt.plot(data[:,0], data[:,3], color='blue', linestyle='--', marker='s', label='Donations to Charity C')
plt.plot(data[:,0], data[:,4], color='black', linestyle='--', marker='d', label='Donations to Charity D')

plt.xlabel('Year', fontsize=12)
plt.ylabel('Donations (Million Dollars)', fontsize=12)
plt.title('Donations to four charities from 2016 to 2019', fontsize=14)
plt.xticks(data[:,0])
plt.legend(loc='best', fontsize=12, ncol=2, frameon=True, fancybox=True, shadow=True)

plt.grid()
plt.tight_layout()

plt.savefig('line chart/png/332.png')
plt.clf()
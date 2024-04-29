
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2018,40,30,20], [2019,35,25,15], [2020,30,20,10], [2021,25,15,5], [2022,20,10,2]])

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(1,1,1)

ax.plot(data[:,0], data[:,1], label = 'Air Pollution', marker = 'o')
ax.plot(data[:,0], data[:,2], label = 'Water Pollution', marker = 'o')
ax.plot(data[:,0], data[:,3], label = 'Soil Pollution', marker = 'o')

ax.set_title('Reduction of Pollution in the Environment from 2018 to 2022')
ax.set_xlabel('Year')
ax.set_ylabel('Pollution Level')

ax.set_xticks(data[:,0])

ax.legend(loc='upper right')
ax.grid(ls='--')

plt.tight_layout()
plt.savefig('line chart/png/26.png')

plt.close()
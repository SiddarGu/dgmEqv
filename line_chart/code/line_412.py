
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 6))
ax = plt.subplot(1,1,1)

ax.plot(np.array([2019, 2020, 2021, 2022]), 
        np.array([[1000, 800, 1200, 1500], 
                  [1200, 900, 1100, 1600], 
                  [800, 1100, 1300, 1200], 
                  [1500, 1200, 1400, 800]]),
        linewidth=2, label=['Crop A','Crop B','Crop C','Crop D'])

ax.set_title('Crop Production in four categories of crops in the United States from 2019-2022')
ax.set_xlabel('Year')
ax.set_ylabel('Tonnes')

ax.grid(True, linestyle='--')
ax.legend(loc=2)

plt.xticks(np.arange(2019, 2023))
plt.tight_layout()
plt.savefig('line chart/png/220.png')
plt.clf()
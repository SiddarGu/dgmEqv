

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6)) 
ax = plt.subplot() 
ax.bar(['2020', '2021', '2022', '2023'], [3.2, 3.5, 3.8, 4.2], width=0.3, color='b', label='Crop Production(billion tons)') 
ax.bar(['2020', '2021', '2022', '2023'], [2.5, 2.7, 3.0, 3.2], width=0.3, color='y', label='Livestock Production(billion tons)', bottom=[3.2, 3.5, 3.8, 4.2]) 
ax.legend(loc='upper center') 
plt.xticks(['2020', '2021', '2022', '2023']) 
plt.title('Crop and Livestock Production from 2020 to 2023') 
plt.tight_layout() 
plt.savefig('bar chart/png/555.png') 
plt.clf()
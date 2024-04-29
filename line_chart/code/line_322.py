
import matplotlib.pyplot as plt
import numpy as np

data = [[2020, 1000, 1200, 900, 1100],
        [2021, 1200, 1000, 1200, 1100],
        [2022, 1300, 1200, 1000, 900],
        [2023, 1100, 1100, 1300, 1200]]

data = np.array(data)
x = data[:,0]
y1, y2, y3, y4 = data[:,1], data[:,2], data[:,3], data[:,4]

fig = plt.figure(figsize=(12, 8))
plt.plot(x, y1, color='red', label='Wheat(bushels)')
plt.plot(x, y2, color='green', label='Rice(bushels)')
plt.plot(x, y3, color='blue', label='Corn(bushels)')
plt.plot(x, y4, color='black', label='Soybeans(bushels)')

plt.title('Crop Production for the Years 2020-2023', fontsize=20, fontweight='bold')
plt.xlabel('Year', fontsize=16)
plt.ylabel('Production', fontsize=16)
plt.xticks(x, rotation=45, fontsize=14, ha='right')
plt.yticks(fontsize=14)
plt.legend(fontsize=14, loc='upper right', bbox_to_anchor=(1.3, 1))

plt.grid(linestyle='-.', linewidth=0.5)
plt.tight_layout()

plt.savefig('line chart/png/435.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

x_data = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
vege_data = [2000, 2200, 2500, 2100, 2400, 2600, 2400, 2300]
grain_data = [3000, 3300, 3500, 3200, 3400, 3600, 3300, 3200]
fruit_data = [4000, 4200, 4500, 4000, 4300, 4800, 4200, 4500]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.plot(x_data, vege_data, color='red', linestyle='-', marker='o', label='Vegetable Production')
ax.plot(x_data, grain_data, color='green', linestyle='-', marker='o', label='Grain Production')
ax.plot(x_data, fruit_data, color='blue', linestyle='-', marker='o', label='Fruit Production')

plt.xticks(np.arange(len(x_data)), x_data, rotation=90)

ax.set_title('Crop production of vegetables, grain and fruits in 2020')
ax.legend(loc='best', fontsize='medium', facecolor='white', framealpha=0.7)

fig.tight_layout()

plt.savefig('line chart/png/226.png')

plt.clf()
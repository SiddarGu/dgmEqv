

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
ax = plt.subplot()

ax.plot(['2020', '2021', '2022', '2023', '2024'], [150, 160, 170, 180, 190], linewidth=3, marker='o', color='red', label='Total Vehicles(in millions)')
ax.plot(['2020', '2021', '2022', '2023', '2024'], [80, 90, 100, 110, 120], linewidth=3, marker='o', color='blue', label='Cars')
ax.plot(['2020', '2021', '2022', '2023', '2024'], [30, 35, 40, 45, 50], linewidth=3, marker='o', color='green', label='Heavy Trucks')
ax.plot(['2020', '2021', '2022', '2023', '2024'], [40, 35, 30, 25, 20], linewidth=3, marker='o', color='orange', label='Light Trucks')

plt.xticks(['2020', '2021', '2022', '2023', '2024'], rotation=45, fontsize=13)
plt.yticks(fontsize=13)

ax.set_title('Increase of vehicle ownership over 5 years in North America', fontsize=18)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Vehicles', fontsize=15)

plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/335.png', format='png')
plt.clf()
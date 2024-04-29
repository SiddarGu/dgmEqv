
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.plot(['2020', '2021', '2022', '2023', '2024', '2025'],
         [4.2, 4.5, 4.8, 5.0, 5.2, 5.5],
         label = 'Carbon Emission',
         linewidth=2)

plt.plot(['2020', '2021', '2022', '2023', '2024', '2025'],
         [20, 25, 30, 35, 40, 45],
         label = 'Renewable Energy Usage',
         linewidth=2)

plt.title('Global Carbon Emission and Renewable Energy Usage Trends from 2020 to 2025', fontsize=12)
plt.xlabel('Year', fontsize=10)
plt.xticks(rotation=45)
plt.ylabel('Values', fontsize=10)
plt.legend(loc='upper left', bbox_to_anchor=(1,1), fontsize=10, ncol=1, frameon=False)

plt.tight_layout()
plt.savefig('line chart/png/91.png')
plt.clf()
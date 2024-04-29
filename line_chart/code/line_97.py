
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
ax = plt.subplot()
ax.set_title('Growth of Tourism in the US from 2018 to 2023') 
ax.set_xlabel('Year')
ax.set_ylabel('Tourist Arrivals(million)')
ax.grid(True)
ax.plot(['2018', '2019', '2020', '2021', '2022', '2023'], 
        [80, 85, 90, 95, 100, 105], color='green', marker='o', label='International Tourist Arrivals')
ax.plot(['2018', '2019', '2020', '2021', '2022', '2023'], 
        [100, 106, 113, 120, 126, 132], color='blue', marker='o', label='Domestic Tourist Arrivals')
ax.legend(loc='upper left', frameon=False)
ax.set_xticks(['2018', '2019', '2020', '2021', '2022', '2023'])
plt.tight_layout()
plt.savefig('line chart/png/114.png')
plt.clf()
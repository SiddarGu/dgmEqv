
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
ax = plt.subplot()
plt.plot(['2020', '2021', '2022', '2023', '2024'], [400000, 450000, 500000, 550000, 600000], marker='o', label='Average Home Price')
plt.plot(['2020', '2021', '2022', '2023', '2024'], [200, 250, 300, 350, 400], marker='o', label='Number of Properties Sold')
plt.title('Home Prices and Property Sales in the US from 2020 to 2024')
plt.xlabel('Year')
plt.ylabel('Price/Number of Properties')
plt.xticks(['2020', '2021', '2022', '2023', '2024'])
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('line chart/png/98.png')
plt.clf()

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot([2020, 2021, 2022, 2023, 2024], [900, 950, 1000, 1200, 1300], label='International tourist arrivals (millions)')
plt.plot([2020, 2021, 2022, 2023, 2024], [1000, 1100, 1200, 1500, 1700], label='Domestic tourist arrivals (millions)')
plt.title('Tourist Arrivals in the US from 2020 to 2024')
plt.xlabel('Year')
plt.ylabel('Tourist arrivals (millions)')
plt.xticks([2020, 2021, 2022, 2023, 2024])
plt.grid(True)
for x,y in zip([2020, 2021, 2022, 2023, 2024], [900, 950, 1000, 1200, 1300]):
    plt.annotate(y, (x,y), rotation=50, ha="center", wrap=True)
for x,y in zip([2020, 2021, 2022, 2023, 2024], [1000, 1100, 1200, 1500, 1700]):
    plt.annotate(y, (x,y), rotation=50, ha="center", wrap=True)
plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/229.png')
plt.clf()
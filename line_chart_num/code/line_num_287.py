
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
Year = [2020, 2021, 2022, 2023]
Rice = [1000, 1100, 1300, 1500]
Wheat = [1200, 1400, 1300, 1100]
Maize = [1300, 1500, 1600, 1800]
plt.plot(Year, Rice, color='#FFA500', linewidth=2, marker='o', label='Rice Production(tonnes)')
plt.plot(Year, Wheat, color='#7FFFD4', linewidth=2, marker='o', label='Wheat Production(tonnes)')
plt.plot(Year, Maize, color='#FFC0CB', linewidth=2, marker='o', label='Maize Production(tonnes)')
plt.xticks(Year, Year, rotation=45)
plt.xlabel('Year')
plt.ylabel('Production (tonnes)')
plt.title('Crop Production in India from 2020 to 2023')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
for x, y in zip(Year, Rice):
    plt.annotate(str(y), xy=(x, y))
for x, y in zip(Year, Wheat):
    plt.annotate(str(y), xy=(x, y))
for x, y in zip(Year, Maize):
    plt.annotate(str(y), xy=(x, y))
plt.tight_layout()
plt.savefig('line chart/png/507.png')
plt.clf()
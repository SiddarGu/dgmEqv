
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

year = [2020, 2021, 2022, 2023, 2024, 2025]
temp = [14, 15, 16, 17, 18, 19]
co2 = [4500, 4600, 4700, 4800, 4900, 5000]

plt.plot(year, temp, label="Average Temperature (°C)") 
plt.plot(year, co2, label="Carbon Emissions (million tons)")

plt.title("Climate Change: Average Temperature and Carbon Emissions from 2020 to 2025")

plt.xlabel("Year")
plt.ylabel("Value")

plt.xticks(year)

plt.legend(loc="upper left")

for a, b in zip(year, temp):
    plt.annotate(str(b), xy=(a, b), fontsize=12, rotation=45, ha='center', va='bottom')

for a, b in zip(year, co2):
    plt.annotate(str(b), xy=(a, b), fontsize=12, rotation=45, ha='center', va='bottom')

plt.tight_layout()
plt.savefig("line chart/png/511.png")
plt.clf()
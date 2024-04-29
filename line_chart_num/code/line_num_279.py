
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(14, 8))

year = np.array([2019, 2020, 2021, 2022, 2023])
windspeed = np.array([5, 6, 7, 8, 9])
solar_radiation = np.array([8, 9, 10, 11, 12])
temperature = np.array([15, 17, 19, 21, 23])

plt.plot(year, windspeed, label="Windspeed (m/s)")
plt.plot(year, solar_radiation, label="Solar Radiation (hundred W/m2)")
plt.plot(year, temperature, label="Temperature (Celsius)")
plt.xticks(year)
plt.title("Climate Change in the Arctic Region: Average Windspeed, Solar Radiation, and Temperature Variations from 2019-2023")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend(loc='upper left')
for a, b, c in zip(year, windspeed, solar_radiation): 
    plt.annotate(str(b) + " m/s", xy=(a, b))
for a, b, c in zip(year, solar_radiation, temperature):
    plt.annotate(str(c) + " W/m2", xy=(a, c))
for a, b, c in zip(year, windspeed, temperature):
    plt.annotate(str(c) + " °C", xy=(a, c))
plt.tight_layout()
plt.savefig("line_279.png")
plt.clf()
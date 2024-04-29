
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6))
ax = plt.subplot()
ax.grid(linestyle='--', linewidth=0.5, color='gray', alpha=0.3)

x = np.arange(2020, 2024, 1)
co2 = [415, 417, 419, 421]
ozone = [320, 321, 322, 323]
nd = [0.061, 0.065, 0.070, 0.073]

plt.plot(x, co2, color='green', label="CO2(ppm)")
plt.plot(x, ozone, color='blue', label="Ozone(ppm)")
plt.plot(x, nd, color='red', label="Nitrogen Dioxide(ppm)")

plt.xlabel("Year", fontdict={'size': 14})
plt.ylabel("Concentrations", fontdict={'size': 14})
plt.title("Air Pollutant Concentrations in the Atmosphere of the United States in 2020-2023", fontdict={'size': 16})
plt.xticks(x, fontsize=12)
plt.legend(frameon=False, fontsize=12)

plt.tight_layout()
plt.savefig("line chart/png/524.png")
plt.clf()
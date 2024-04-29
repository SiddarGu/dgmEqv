

import matplotlib.pyplot as plt
import numpy as np

Region = ["North America", "Europe", "Asia"]
Wind_Energy = [500, 400, 700]
Solar_Energy = [250, 200, 450]
Hydro_Energy = [100, 150, 200]

x = np.arange(len(Region))

total_width, n = 0.8, 3
width = total_width / n

plt.figure(figsize=(12,6))

ax = plt.subplot(1,1,1)
ax.bar(x-width, Wind_Energy, width=width, label="Wind Energy (GW)")
ax.bar(x, Solar_Energy, width=width, label="Solar Energy (GW)")
ax.bar(x+width, Hydro_Energy, width=width, label="Hydro Energy (GW)")

ax.set_xticks(x)
ax.set_xticklabels(Region)

ax.set_title("Energy sources in three regions in 2021")
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig("bar chart/png/84.png")
plt.clf()
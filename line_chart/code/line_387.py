
import matplotlib.pyplot as plt
import numpy as np

Month = ["January", "February", "March", "April"] 
Wind_Energy = [1000, 1100, 1200, 1300] 
Solar_Energy = [1200, 1300, 1400, 1500] 
Nuclear_Energy = [1500, 1400, 1600, 1700]
Hydro_Energy = [1300, 1200, 1100, 1000]

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(Month, Wind_Energy, color="red", marker="o", label="Wind Energy")
ax.plot(Month, Solar_Energy, color="green", marker="o", label="Solar Energy")
ax.plot(Month, Nuclear_Energy, color="blue", marker="o", label="Nuclear Energy")
ax.plot(Month, Hydro_Energy, color="orange", marker="o", label="Hydro Energy")
ax.set_title("Energy consumption of different sources in April 2021")
ax.legend(loc="lower right")
plt.xticks(Month)
plt.tight_layout()
plt.savefig('line chart/png/193.png')
plt.clf()
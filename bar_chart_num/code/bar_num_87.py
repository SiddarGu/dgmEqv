
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA","UK","Germany","France"]
SolarEnergy = [1000, 900, 1100, 800]
WindEnergy = [1200, 1300, 1400, 1500]
HydroEnergy = [800, 1100, 1200, 1400]

x = np.arange(len(Country))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(x-width, SolarEnergy, width, label="SolarEnergy (MW)")
ax.bar(x, WindEnergy, width, label="WindEnergy (MW)")
ax.bar(x+width, HydroEnergy, width, label="HydroEnergy (MW)")
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_title("Renewable energy production in four countries in 2021")
ax.legend()

for i in range(len(Country)):
    ax.text(x[i] - 0.1, SolarEnergy[i] + 10, str(SolarEnergy[i]), color="black")
    ax.text(x[i] + 0.1, WindEnergy[i] + 10, str(WindEnergy[i]), color="black")
    ax.text(x[i] + 0.3, HydroEnergy[i] + 10, str(HydroEnergy[i]), color="black")
plt.tight_layout()
plt.savefig("Bar Chart/png/185.png")
plt.clf()
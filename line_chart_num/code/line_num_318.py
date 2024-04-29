
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

data = [[2020, 1000, 5], [2021, 1200, 6], [2022, 1500, 7], [2023, 1100, 8], [2024, 1800, 9], [2025, 2000, 10]]

x = np.arange(len(data))
co2_emission = [row[1] for row in data]
deforestation_rate = [row[2] for row in data]

ax.plot(x, co2_emission, label="CO2 Emission(tons)", color='b', marker='o', linestyle='dashed', linewidth=1, markersize=10)
ax.plot(x, deforestation_rate, label="Deforestation Rate(%)", color='r', marker='o', linestyle='dashed', linewidth=1, markersize=10)

ax.set_title("Global CO2 Emission and Deforestation Rate in 2020-2025")
ax.set_xlabel("Year")
ax.set_xticks(x)
ax.set_xticklabels([row[0] for row in data], rotation=45)
ax.grid(True, linestyle='--', linewidth=0.5, color='gray')

j = 0
for x, y1, y2 in data:
    ax.annotate(str(y1), xy=(j, y1), xytext=(-15, 5), textcoords='offset points')
    ax.annotate(str(y2), xy=(j, y2), xytext=(-15, 5), textcoords='offset points')
    j+=1

ax.legend(loc='lower right')

plt.tight_layout()
plt.savefig('line chart/png/43.png')
plt.clf()
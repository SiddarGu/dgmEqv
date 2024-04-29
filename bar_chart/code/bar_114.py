
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
x_position = np.arange(4)
renewable_energy = [20, 25, 30, 35]
co2_emission = [1000, 900, 800, 700]

plt.bar(x_position, renewable_energy, label="Renewable Energy(%)", color='#4EA0D3', edgecolor='#235F9C', width=0.3)
plt.bar(x_position + 0.3, co2_emission, label="CO2 Emission(Tonnes)", color='#E58A8A', edgecolor='#B94F4F', width=0.3)

plt.xticks(x_position, ['USA', 'UK', 'Germany', 'France'], fontsize=12)
plt.yticks(fontsize=12)
plt.title('Percentage of renewable energy and CO2 emission of four countries in 2021', fontsize=15)
plt.legend(fontsize=12, loc="upper right")
plt.tight_layout()
plt.savefig("bar chart/png/328.png")
plt.clf()
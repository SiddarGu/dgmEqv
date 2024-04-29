
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()

# Data
energy_sources = ["Renewable", "Nuclear", "Fossil Fuel", "Hydroelectric", "Geothermal"]
energy_percent = np.array([50, 20, 20, 5, 5])

# Plot
ax.pie(energy_percent, labels=energy_sources, autopct='%1.1f%%',
        textprops={'fontsize': 14, 'fontweight': 'bold'},
        wedgeprops={'edgecolor': 'black'})

# Legend
ax.legend(energy_sources, loc="upper right", bbox_to_anchor=(1.25, 1))

# Title
plt.title("Energy Sources Distribution in the USA, 2023", fontsize=18)

# Save
plt.tight_layout()
plt.savefig('pie chart/png/374.png', dpi=400)
plt.clf()
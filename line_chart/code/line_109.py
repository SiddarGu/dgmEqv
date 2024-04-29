
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

month=['January','February','March','April','May','June','July','August']
energy_output=[80,82,84,79,81,85,82,87]
carbon_emissions=[40000,45000,42000,41000,43000,42000,45000,44000]

ax.plot(month,energy_output,label='Energy Output (GWh)',marker='o')
ax.plot(month,carbon_emissions,label='Carbon Emissions (kg)',marker='s')
ax.legend(loc='best')
ax.set_title('Energy output and carbon emissions in a renewable energy plant in 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Energy Output/Carbon Emissions (GWh/kg)')
ax.set_xticks(month)
ax.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/393.png')
plt.clf()
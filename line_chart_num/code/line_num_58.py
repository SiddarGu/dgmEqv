
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Set font
plt.rcParams['font.sans-serif'] = "SimHei"

# Set axis
x = np.array([2015, 2016, 2017, 2018, 2019])
CO2_Emission = np.array([100, 150, 180, 210, 240])
Renewable_Energy_Consumption = np.array([50, 80, 100, 120, 150])

ax.set_title('Annual CO2 Emission and Renewable Energy Consumption in the US from 2015 to 2019')
ax.set_xlabel('Year')
ax.set_ylabel('CO2 Emission (tons) & Renewable Energy Consumption (GWh)')
ax.set_xticks(x)

# Plot
ax.plot(x, CO2_Emission, label='CO2 Emission', color="red", marker="o")
ax.plot(x, Renewable_Energy_Consumption, label='Renewable Energy Consumption', color="green", marker="o")

# Annotate
for i in range(5):
    ax.annotate('  Carbon Footprint: %s' % (CO2_Emission[i] - Renewable_Energy_Consumption[i]),
                xy=(x[i], CO2_Emission[i]),
                xytext=(x[i], CO2_Emission[i] + 5),
                rotation=90,
                fontsize=10,
                color='#339933',
                arrowprops=dict(facecolor='#339933', shrink=0.05))

# Display legend
ax.legend(loc='upper left', bbox_to_anchor=(0.03, 0.97), ncol=2, shadow=True)

# Display background grid
plt.grid(alpha=0.3)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save image
plt.savefig('line chart/png/251.png')

# Clear current image state
plt.cla()
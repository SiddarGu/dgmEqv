
import matplotlib.pyplot as plt
import numpy as np

# Set the figure size
plt.figure(figsize=(10, 6))

# Set the title
plt.title("Renewable Energy Production in the US from 2017 to 2021")

# Set the x-axis
x_data = np.array([2017, 2018, 2019, 2020, 2021])

# Set the y-axis
y_data_solar = np.array([1000, 1100, 1300, 1500, 1800])
y_data_wind = np.array([500, 800, 900, 1100, 1300])
y_data_hydro = np.array([1500, 1300, 1400, 1600, 1700])

# Draw the line chart
plt.plot(x_data, y_data_solar, label="Solar Energy(kW/hr)", color="red", linewidth=1.5, marker='o')
plt.plot(x_data, y_data_wind, label="Wind Energy(kW/hr)", color="green", linewidth=1.5, marker='o')
plt.plot(x_data, y_data_hydro, label="Hydro Energy(kW/hr)", color="blue", linewidth=1.5, marker='o')

# Set the xticks
plt.xticks(x_data)

# Set the legend position
plt.legend(loc='upper left')

# Label each data point
for x_point, y_point_solar, y_point_wind, y_point_hydro in zip(x_data, y_data_solar, y_data_wind, y_data_hydro):
    plt.annotate(f'{y_point_solar}/{y_point_wind}/{y_point_hydro}', xy=(x_point, y_point_solar), xytext=(0, 5), textcoords="offset points", fontsize=9)

# Set the background grid
plt.grid(True, linewidth=0.2)

# Save the figure
plt.savefig(r'line chart/png/42.png', bbox_inches='tight')

# Clear the current image state
plt.clf()
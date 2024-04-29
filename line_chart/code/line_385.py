
import matplotlib.pyplot as plt 
import numpy as np

# Set figure size
plt.figure(figsize=(10,6))

# Add subplot
ax = plt.subplot()

# Define data
year = [2020, 2021, 2022, 2023]
Average_Global_Temperature = [1.2, 1.3, 1.5, 1.4]
Sea_Level_Rise = [3.3, 3.4, 3.5, 3.6]
CO2_in_Atmosphere = [412, 415, 417, 420]

# Plot line chart
ax.plot(year, Average_Global_Temperature, label='Average Global Temperature (Celsius)', marker='o')
ax.plot(year, Sea_Level_Rise, label='Sea Level Rise (mm)', marker='o')
ax.plot(year, CO2_in_Atmosphere, label='CO2 in Atmosphere (ppm)', marker='o')

# Set ticks of x axis
plt.xticks(np.arange(2020, 2024, step=1))

# Add title
plt.title('Global Climate Change from 2020-2023')

# Display legend
ax.legend(loc='best')

# Automatically resize the image
plt.tight_layout() 

# Save the image
plt.savefig('line chart/png/352.png')

# Clear the current image state
plt.clf()
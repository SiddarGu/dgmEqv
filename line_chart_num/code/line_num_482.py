
import matplotlib.pyplot as plt
import pandas as pd

# Create the data
data = {'Temperature (Celsius)': [20, 25, 30, 35, 40, 45, 50], 
        'Viscosity (Pa-s)': [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07], 
        'Pressure (Kpa)': [90, 100, 110, 120, 130, 140, 150], 
        'Relative Humidity (%)': [20, 30, 40, 50, 60, 70, 80]}

# Create the dataframe
df = pd.DataFrame(data)

# Create the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Plot the data
ax.plot(df['Temperature (Celsius)'], df['Viscosity (Pa-s)'], marker='o', linestyle='-', color='blue', label='Viscosity (Pa-s)')

# Add the labels to the points
for i, txt in enumerate(df['Viscosity (Pa-s)']):
    ax.annotate(txt, (df['Temperature (Celsius)'][i], df['Viscosity (Pa-s)'][i]), fontsize=14)

# Set the title
ax.set_title('Viscosity of a sample of oil at different temperatures and relative humidities', fontsize=16)

# Add the legend
ax.legend(loc='best')

# Add the background grids
ax.grid(linestyle='--', alpha=0.3)

# Set the xticks
ax.set_xticks(df['Temperature (Celsius)'])

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/564.png')

# Clear the current image state
plt.clf()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Represent the data using a dictionary
data = {
    'Year': [2016, 2017, 2018, 2019, 2020],
    'Hotel Stays (%)': [30, 35, 40, 45, 50],
    'Vacation Rentals (%)': [20, 25, 30, 35, 40],
    'Airbnb Stays (%)': [25, 20, 15, 10, 5],
    'Resort Stays (%)': [15, 10, 10, 5, 5],
    'Cruise Ship Bookings (%)': [10, 10, 5, 5, 0]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Ceil max total value up to nearest multiple of 10, 100 or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y axis range and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df['Year'], df['Hotel Stays (%)'], df['Vacation Rentals (%)'], df['Airbnb Stays (%)'], df['Resort Stays (%)'], df['Cruise Ship Bookings (%)'], labels=['Hotel Stays', 'Vacation Rentals', 'Airbnb Stays', 'Resort Stays', 'Cruise Ship Bookings'], colors=['steelblue', 'orange', 'green', 'red', 'purple'], alpha=0.8)

# Set x axis range and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(range(len(df.index)))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')

# Set grid lines
ax.grid(linestyle='dotted', linewidth=1, color='lightgrey')

# Set legend and position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title
ax.set_title('Hospitality Trends by Year')

# Automatically resize image
plt.tight_layout()

# Save the chart
plt.savefig('output/final/area_chart/png/20231228-131755_65.png', bbox_inches='tight')

# Clear current image state
plt.clf()
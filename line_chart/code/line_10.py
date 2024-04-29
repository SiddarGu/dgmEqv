

import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))

# Data
year = [2020, 2021, 2022, 2023, 2024]
price_per_sqm = [800, 850, 900, 950, 1000]
rental_price_per_month = [1200, 1300, 1400, 1500, 1600]

# Plot
plt.plot(year, price_per_sqm, label='Price per Square Meter (USD)')
plt.plot(year, rental_price_per_month, label='Rental Price per Month (USD)')

# Legend
plt.legend(loc='upper left')

# Labels
plt.xlabel('Year')
plt.ylabel('Price (USD)')

# Title
plt.title('Housing prices and rental prices in US cities between 2020-2024', fontsize=13)

# Ticks
plt.xticks(year)

# Resize
plt.tight_layout()

# Save
plt.savefig('line chart/png/550.png')

# Clear
plt.clf()
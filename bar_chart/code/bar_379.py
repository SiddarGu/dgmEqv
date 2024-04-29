
import matplotlib.pyplot as plt
import numpy as np

# Set title and figure size
plt.figure(figsize=(10,8))
plt.title("Average House and Apartment Prices in Four Regions in 2021")

# Set data
region = ['Southeast', 'Northeast', 'Midwest', 'Southwest']
house_price = [400000, 370000, 350000, 410000]
apartment_price = [200000, 220000, 210000, 230000]

# Plot bar chart
plt.bar(region, house_price, label='House Price', bottom=apartment_price)
plt.bar(region, apartment_price, label='Apartment Price')

# Set legend
plt.legend(loc='upper right')

# Set x ticks
plt.xticks(rotation=45, ha='right')

# Resize image
plt.tight_layout()

# Save image
plt.savefig('bar chart/png/130.png')

# Clear state
plt.clf()
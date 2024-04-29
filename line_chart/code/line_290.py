
import matplotlib.pyplot as plt
import numpy as np

# Get the data
year = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007])
home_price = np.array([200, 250, 300, 350, 400, 450, 500])
rental_price = np.array([50, 60, 70, 80, 90, 100, 110])

# Create figure and plot
fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(year, home_price, label='Home Price', color='red')
ax.plot(year, rental_price, label='Rental Price', color='blue')

# Set legend
ax.legend()

# Set title
ax.set_title('Changes in Average Home and Rental Prices from 2001 to 2007')

# Set x-axis label
ax.set_xlabel('Year')

# Set y-axis label
ax.set_ylabel('Price (thousand dollars)')

# Set x-axis labels
plt.xticks(year)

# Save the figure
plt.savefig('line chart/png/345.png')

# Clear the current image state
plt.clf()
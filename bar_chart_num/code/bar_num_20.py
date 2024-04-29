
import matplotlib.pyplot as plt
import numpy as np

# Set up the data
Country = ['USA', 'UK', 'Germany', 'France']
Food = [3000, 4500, 4000, 3500]
Beverage = [4500, 6000, 5000, 4800]

# Create figure
fig = plt.figure(figsize=(8, 6))

# Plot bar chart
ax = fig.add_subplot(111)
ax.bar(Country, Food, bottom=Beverage, label='Food Production', align='center')
ax.bar(Country, Beverage, label='Beverage Production', align='center')


# Set the title of the figure
plt.title('Food and Beverage Production in four countries in 2021', fontsize=14)

# Set the legend
ax.legend(loc='best')

# Adjust the position of the x-axis label
ax.set_xticks(Country)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('bar_20.png')

# Clear the current image state
plt.clf()
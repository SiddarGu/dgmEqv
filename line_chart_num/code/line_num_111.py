
import matplotlib.pyplot as plt
import numpy as np

# Set the figure size
plt.figure(figsize=(8, 6))

# Define the variables
year = [2009, 2010, 2011, 2012]
retail_sales = [1000, 1200, 1400, 1600]
online_sales = [200, 400, 600, 800]
total_sales = [1200, 1600, 2000, 2400]

# Plot the data
plt.plot(year, retail_sales, label='Retail Sales')
plt.plot(year, online_sales, label='Online Sales')
plt.plot(year, total_sales, label='Total Sales')

# Label the x-axis
plt.xticks(year, rotation=45)

# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Sales (million dollars)')
plt.title('Yearly trend in retail and online sales')
plt.legend(loc='best')

# Add annotations
for x, y in zip(year, retail_sales):
    plt.annotate(str(y), xy=(x, y))
for x, y in zip(year, online_sales):
    plt.annotate(str(y), xy=(x, y))
for x, y in zip(year, total_sales):
    plt.annotate(str(y), xy=(x, y))

# Use tight_layout() for automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/396.png')

# Clear the current image state
plt.clf()
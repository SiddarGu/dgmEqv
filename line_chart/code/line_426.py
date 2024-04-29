
import matplotlib.pyplot as plt 

# Create figure and adjust figsize
fig = plt.figure(figsize=(10, 6))

# Set the data
Year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]
Renewable_Energy = [100, 120, 150, 180, 210, 240, 270, 300, 330]
Non_Renewable_Energy = [900, 800, 700, 600, 500, 400, 300, 200, 100]

# Plot the graph
plt.plot(Year, Renewable_Energy, '-o', color='green', label='Renewable Energy(kWh)')
plt.plot(Year, Non_Renewable_Energy, '-o', color='red', label='Non-Renewable Energy(kWh)')

# Set the position of the legend
plt.legend(loc='lower right')

# Set the axes labels
plt.xlabel('Year')
plt.ylabel('kWh')

# Set the ticks
plt.xticks(Year, rotation=90)

# Set the title
plt.title('Comparison of Renewable and Non-Renewable Energy Usage in the US from 2000 to 2008')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/434.png')

# Clear the current image state
plt.clf()
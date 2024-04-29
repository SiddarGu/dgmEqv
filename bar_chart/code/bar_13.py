
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10, 5))

# Set data
Country = ['USA', 'UK', 'Germany', 'France']
Renewable_Energy = [50, 65, 80, 70]
Total_Energy = [450, 500, 480, 470]

# Plot
ax = plt.subplot()
ax.bar(Country, Renewable_Energy, label='Renewable Energy', color='green', bottom=0)
ax.bar(Country, Total_Energy, label='Total Energy', color='grey', bottom=Renewable_Energy)

# Adjust x-axis
plt.xticks(Country, rotation=60, wrap=True)

# Set title and legend
plt.title('Renewable energy production compared to total energy production in four countries in 2021')
plt.legend(loc='upper center')

# Adjust figure size
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/326.png')

# Clear figure
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

# Create data
Region = ['North America','Europe','Asia','Africa']
CO2_Emission = [10,5,20,15]
Renewable_Energy = [30,50,15,25]

# Create figure
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# Plot bar chart
width = 0.4
ax.bar(np.arange(len(CO2_Emission)),CO2_Emission,width,label='CO2 Emission(kg/capita)',color='blue')
ax.bar(np.arange(len(Renewable_Energy))+width,Renewable_Energy,width,label='Renewable Energy Sources(%)',color='orange')

# Set title
ax.set_title('CO2 Emission and Renewable Energy Sources Usage in four regions in 2021',fontsize=14)

# Set xticks
ax.set_xticks(np.arange(len(Region))+width/2)
ax.set_xticklabels(Region, rotation=45, wrap=True)

# Add legend
ax.legend(loc='best')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/421.png', dpi=500)

# Clear current figure
plt.clf()
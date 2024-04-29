
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig=plt.figure(figsize=(10,6))

# Set Data
countries = ['USA', 'UK', 'Germany', 'France']
renewable_energy = [300000, 250000, 350000, 200000]
non_renewable_energy = [500000, 550000, 450000, 400000]

# Add subplot
ax = fig.add_subplot()

# Set width
barWidth = 0.3

# Plot bar
ax.bar(np.arange(len(countries)), renewable_energy, width=barWidth, label='Renewable Energy(kWh)', color='#ffa500')
ax.bar(np.arange(len(countries)) + barWidth, non_renewable_energy, width=barWidth, label='Non-Renewable Energy(kWh)', color='#c2c2d6')

# Label x-axis
ax.set_xticks(np.arange(len(countries)) + barWidth/2)
ax.set_xticklabels(countries)

# Add title and legend
plt.title('Comparison of renewable and non-renewable energy consumption in four countries in 2021')
plt.legend()

# Annotate value
for i in range(len(countries)):
    ax.annotate('({}, {})'.format(renewable_energy[i], non_renewable_energy[i]), 
                xy=(i + barWidth/2, renewable_energy[i]), 
                xytext=(0, 3), 
                textcoords="offset points", 
                ha='center', va='bottom',
                rotation=90)

plt.tight_layout()
plt.savefig('Bar Chart/png/113.png')
plt.clf()
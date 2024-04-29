

import matplotlib.pyplot as plt
import numpy as np

#Create figure
plt.figure(figsize=(10,6))

# Define data 
Organization = ['Red Cross', 'UNICEF', 'World Vision', 'Greenpeace']
Donations = [50, 45, 40, 35]
Volunteers = [3000, 2500, 2000, 1500]

# plot bar chart
x = np.arange(len(Organization))
width = 0.35
plt.bar(x, Donations, width=width, label='Donations(million)', color='#539caf')
plt.bar(x+width, Volunteers, width=width, label='Volunteers', color='#7663b0')

# Set label
plt.xlabel('Organization', fontsize=12)
plt.ylabel('Numbers', fontsize=12)

# Add xticks
plt.xticks(x+width/2, Organization, rotation=45, fontsize=12)

# Add legend
plt.legend(loc='best', fontsize=12)

# Set title
plt.title('Donations and volunteers for four charity organizations in 2021', fontsize=15)

# Fit figure size and save image
plt.tight_layout()
plt.savefig('bar chart/png/40.png')

# Clear current image state
plt.clf()
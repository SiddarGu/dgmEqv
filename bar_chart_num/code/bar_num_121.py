
import matplotlib.pyplot as plt 
import numpy as np 

# Create figure 
fig = plt.figure(figsize=(12,6))

# Create data
Country = ['USA', 'UK', 'Germany', 'France']
Hospitals = [500, 200, 300, 400]
Pharmacies = [3000, 1000, 2000, 2500]
Clinics = [5000, 3000, 4000, 4500]

# Create bars 
ax = fig.add_subplot(1, 1, 1)
ax.bar(Country, Hospitals, color='blue', label='Hospitals')
ax.bar(Country, Pharmacies, bottom=Hospitals, color='red', label='Pharmacies')
ax.bar(Country, Clinics, bottom=np.array(Hospitals)+np.array(Pharmacies), color='green', label='Clinics')

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

# Set x label
ax.set_xlabel('Country')

# Set y label
ax.set_ylabel('Number of healthcare facilities')

# Set title
ax.set_title('Number of healthcare facilities in four countries in 2021')

# Set x ticks
ax.set_xticks(Country)

# Set labels for bars
for i, v in enumerate(Hospitals):
    ax.text(i-.15, v/2, str(v), fontweight='bold', fontsize=12, color='white')
for i, v in enumerate(Pharmacies):
    ax.text(i-.15, Hospitals[i] + v/2, str(v), fontweight='bold', fontsize=12, color='white')
for i, v in enumerate(Clinics):
    ax.text(i-.15, Hospitals[i] + Pharmacies[i] + v/2, str(v), fontweight='bold', fontsize=12, color='white')

# Resize figure
fig.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/169.png')

# Clear figure
plt.clf()
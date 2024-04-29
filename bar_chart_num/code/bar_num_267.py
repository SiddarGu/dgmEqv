
import matplotlib.pyplot as plt 
import numpy as np 

# Create data
area = np.array(['North America','Europe','Asia','Africa'])
house_cost = np.array([400000,500000,300000,200000])
rent = np.array([1000,1100,900,800])

# Create figure
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111)

# Draw bar chart
ax.bar(area, house_cost, color='r',label='House Cost')
ax.bar(area, rent, color='b', bottom=house_cost, label='Rent')
plt.legend()

# Set title and labels
ax.set_title('Average house cost and rent in four regions in 2021')
ax.set_xlabel('Area')
ax.set_ylabel('Cost($)')

# Set tick labels
ax.set_xticks(area)

# Add value label on each segment
for hc,r,a in zip(house_cost,rent,area):
    ax.text(a, hc/2, str(hc), ha='center', color='white', fontsize=10)
    ax.text(a, hc+r/2, str(r), ha='center', color='white', fontsize=10)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/134.png')

# Clear figure
plt.clf()
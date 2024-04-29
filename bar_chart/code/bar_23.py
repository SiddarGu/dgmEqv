
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8,6))

# Create data
types = ['Fruits', 'Vegetables', 'Dairy']
retail = [2.50, 3.00, 4.00]
wholesale = [1.50, 2.00, 3.00]

# Create bar chart
ax = fig.add_subplot()
ax.bar(types, retail, label='Retail', bottom=0)
ax.bar(types, wholesale, label='Wholesale', bottom=retail)

# Add legend and title
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
ax.set_title('Retail and Wholesale Prices of Fruits, Vegetables, and Dairy Products in 2021', fontsize=20)

# Add axes labels
ax.set_xlabel('Type', fontsize=15)
ax.set_ylabel('Price (US$/kg)', fontsize=15)

# Setting ticks
ax.set_xticks(np.arange(len(types)))
ax.set_xticklabels(types)

# Automatically resize the image
fig.tight_layout()

# Save image
fig.savefig('bar chart/png/161.png', bbox_inches='tight')

# Clear current image
plt.clf()
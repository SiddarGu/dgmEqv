
import matplotlib.pyplot as plt

# Assign data
Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']
Productivity = [40, 45, 55, 60, 65, 70, 75, 80, 75, 70, 65, 60]
Quantity_Produced = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Plot line chart
ax.plot(Month, Productivity, label='Productivity', marker='o')
ax.plot(Month, Quantity_Produced, label='Quantity Produced', marker='o')

# Set Legend
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

# Add Title
ax.set_title('Annual Productivity and Quantity Produced of a Manufacturing Unit in 2021')

# Set xticks
ax.set_xticks(Month)
ax.set_xticklabels(Month, rotation=60, ha='right', wrap=True)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/427.png')

# Clear current image
plt.clf()

import matplotlib.pyplot as plt

# Create Figure 
plt.figure(figsize=(8,8))

# Create Axes 
ax = plt.subplot()

# Create data 
types = ['Solar', 'Wind', 'Hydro', 'Nuclear']
consumption = [50, 60, 80, 90]
generation = [60, 70, 90, 100]

# Plot Bar Chart
ax.bar(types, consumption, label='Consumption', bottom=0)
ax.bar(types, generation, label='Generation', bottom=consumption)

# Label Axes
ax.set_xlabel('Type')
ax.set_ylabel('GW')

# Add Legend
ax.legend(loc='upper left')

# Add Title
ax.set_title('Energy consumption and generation in four categories in 2021')

# Set Ticks 
ax.set_xticks(types)

# Adjust Figure 
plt.tight_layout()

# Save Figure 
plt.savefig('bar chart/png/16.png')

# Clear Figure
plt.clf()
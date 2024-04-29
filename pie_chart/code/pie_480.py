
import matplotlib.pyplot as plt

# Create Figure
fig, ax = plt.subplots(figsize=(10, 8))

# Data
Segment = ["Fast Food", "Grocery Stores", "Restaurants", "Convenience Stores", "Cafes"]
Percentage = [25, 30, 20, 15, 10]

# Plot 
ax.pie(Percentage, labels=Segment, autopct='%1.1f%%', textprops={'wrap': True, 'rotation': 90})
plt.title('Distribution of Food and Beverage Industry in the USA, 2023')

# Save
plt.tight_layout()
plt.savefig('pie chart/png/463.png')
plt.show()
plt.clf()
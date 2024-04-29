

import matplotlib.pyplot as plt

# Create figure
plt.figure(figsize=(8, 8))

# Create data
products = ["Fruits", "Vegetables", "Dairy", "Bakery", "Meat and Seafood"]
sizes = [25, 20, 15, 20, 20]

# Create a pie chart
plt.pie(sizes, labels=products, autopct='%1.1f%%', startangle=90, shadow=True)

# Set title
plt.title("Food and Beverage Industry Distribution in the USA, 2023")

# Set legend 
plt.legend(products, loc="best", bbox_to_anchor=(1, 0, 0.5, 1))

# Resize image
plt.tight_layout()

# Save figure
plt.savefig("pie chart/png/50.png")

# Clear current image
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10,10))

# Create subplot
ax = plt.subplot()

# Set data
products = ["Dairy Products", "Bakery Products", "Processed Foods", "Confectionary Products", "Fruits and Vegetables", "Canned Foods", "Grains", "Other"]
percentage = [25, 20, 15, 10, 20, 10, 5, 5]

# Plot pie chart
ax.pie(percentage, labels=products, autopct='%.0f%%', pctdistance=0.8, labeldistance=1.1)

# Set chart title
ax.set_title("Distribution of Food and Beverage Products in the Global Market, 2023")
plt.tight_layout()

# Save as image
plt.savefig('pie chart/png/81.png')

# Clear the current image state
plt.clf()
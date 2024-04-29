
import matplotlib.pyplot as plt

# Create figure
plt.figure(figsize=(6,6))

# Plot the data
labels = ["Cereals", "Fruits and Vegetables", "Dairy Products", "Beef", "Poultry", "Other Protein Sources", "Other"]
sizes = [30, 20, 15, 10, 10, 10, 5]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Agricultural Production in the USA, 2023")
plt.axis('equal')

# Save the figure
plt.savefig("pie chart/png/429.png")

# Clear the current image state
plt.clf()
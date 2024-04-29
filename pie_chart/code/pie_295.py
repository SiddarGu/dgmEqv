
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Set data
products = ['Alcoholic Beverages', 'Dairy Products', 'Fruits and Vegetables', 'Sweets and Candy', 'Snacks', 'Other']
percentage = [30, 25, 20, 10, 10, 5]

# Plot Pie Chart
ax.pie(percentage, labels=products, autopct='%1.1f%%', textprops={'fontsize': 15}, 
       shadow=True, startangle=90, rotatelabels=True, labeldistance=1.2)

# Add Title
plt.title('Distribution of Food and Beverage Products in the USA, 2023', fontsize=18)

# Tight Layout
plt.tight_layout()

# Save Figure
plt.savefig("pie chart/png/4.png")

# Clear
plt.clf()
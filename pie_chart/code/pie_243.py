
import matplotlib.pyplot as plt

# Set figure size
plt.figure(figsize=(10, 10))

# Create pie chart
products = ["Dairy Products","Meat and Fish", "Fruits and Vegetables", "Grains and Legumes", "Processed Foods"]
proportion = [30, 15, 25, 20, 10]
plt.pie(proportion, labels = products, autopct='%1.1f%%', shadow = True, startangle = 90)

# Set title and adjust parameters
plt.title("Composition of Food and Beverage Industry in the USA, 2023", fontsize = 20, fontweight = 'bold')
plt.tight_layout()
plt.xticks(rotation=45)

# Save and display plot 
plt.savefig('pie chart/png/529.png')
plt.show()

# Clear the current image state
plt.clf()
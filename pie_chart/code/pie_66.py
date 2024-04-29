
import matplotlib.pyplot as plt

# Create figure
fig=plt.figure(figsize=(10,8))

# Data
crops=["Rice","Wheat","Maize","Soybean","Sorghum","Barley","Millet","Oats"]
percentage=[25,20,15,10,10,10,5,5]

# Plot Pie Chart
plt.pie(percentage,labels=crops,autopct='%1.1f%%',textprops={'fontsize': 14,'wrap':True,'rotation':45},labeldistance=1.1)

# Set Title
plt.title("Major Crop Production in the USA, 2023",fontsize=14)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('pie chart/png/246.png')

# Clear the current image state
plt.clf()
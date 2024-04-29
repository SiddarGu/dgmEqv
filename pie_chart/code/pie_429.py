
import matplotlib.pyplot as plt
import matplotlib

# Create figure
fig = plt.figure(figsize=(8, 8))
ax=fig.add_subplot(111)

# Data
products=['Bakery','Dairy','Soft Drinks','Meat','Fruits and Vegetables','Seafood']
percentage=[25,20,20,10,15,10]

# Pie plot
ax.pie(percentage, labels=products,autopct='%1.1f%%',shadow=True,startangle=90,textprops={'fontsize': 10,'color':'black'})

# Legend
ax.legend(products,bbox_to_anchor=(1, 0.5), loc="center left", fontsize=10)

# Title
plt.title('Distribution of Food and Beverage Products in the USA, 2023', fontsize=16, color='black')

# Adjust the position of the chart
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/212.png')

# Clear the current image state
plt.clf()
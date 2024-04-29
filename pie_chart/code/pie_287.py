
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 8))

# Plot the pie chart
labels = ['Clothing and Apparel', 'Electronics', 'Home Appliances', 'Footwear', 'Accessories', 'Other']
sizes = [45, 20, 8, 10, 12, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
plt.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')

# Set the title of the figure
plt.title('Distribution of Products Sold Online in 2023', fontsize=16)

# Display legend
plt.legend(loc='lower right', bbox_to_anchor=(1.2, 0.5))

# Display the chart
plt.tight_layout()
plt.xticks(rotation=45)

# Save the chart with absolute path
plt.savefig('pie chart/png/123.png')

# Clear the current image state
plt.cla()


import matplotlib.pyplot as plt
import numpy as np

Types = ["Dairy Products", "Fruits and Vegetables", "Meat and Poultry", "Grains and Cereals", "Processed Foods", "Other"]
percentage = [20, 25, 15, 25, 15, 0]

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(percentage, labels=Types, autopct='%1.1f%%', textprops={'fontsize': 10, 'wrap': True}, startangle=90)
ax.axis('equal')
ax.set_title('Distribution of Food and Beverage Types in the US, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/23.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

products = ['Dairy', 'Meat', 'Fruits', 'Vegetables', 'Bakery', 'Grains', 'Snack Foods', 'Beverages', 'Seafood', 'Processed Foods', 'Other']
percentage = [20, 15, 13, 12, 10, 10, 7, 7, 5, 5, 5]

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title('Distribution of Food and Beverage Industry in 2023', fontsize=14)
explode = np.zeros(len(products))
explode[0] = 0.1
ax.pie(percentage, labels=products, explode=explode, autopct='%1.1f%%')
ax.legend(bbox_to_anchor=(1.1, 0.9))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/109.png')
plt.clf()
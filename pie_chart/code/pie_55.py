
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7, 7))
category = ['Fresh Produce', 'Packaged Food', 'Meat and Seafood', 'Dairy Products', 'Beverages']
percentage = [35, 20, 15, 15, 15]
explode = (0, 0, 0, 0, 0)

plt.pie(percentage, explode=explode, labels=category, autopct='%1.1f%%', shadow=False, startangle=90)
plt.title('Distribution of Food and Beverage Products in the Global Market, 2023', fontsize=10, wrap=True, pad=10)
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/74.png', bbox_inches='tight')
plt.close()
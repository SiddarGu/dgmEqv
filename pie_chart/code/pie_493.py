

import matplotlib.pyplot as plt
import numpy as np

causes = ["Education", "Health","Children","Poverty Alleviation", "Human Rights", "Animal Welfare","Environment"]
percentage = [25, 20, 15, 15, 10, 10, 5]

plt.figure(figsize=(6,6))
ax = plt.subplot()
ax.pie(percentage, labels=causes, autopct='%1.1f%%', startangle=90, shadow=True, wedgeprops = {"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})
plt.title('Distribution of Donations to Nonprofit Organizations in 2023')
ax.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/452.png')
plt.clf()
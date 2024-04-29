
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 8))
ax1 = plt.subplot()

Types_of_Homes = ['Single Family Homes', 'Townhomes', 'Condominiums', 'Multi-Family Homes', 'Mobile Homes']
Percentage = [50, 20, 20, 5, 5]

ax1.pie(Percentage, labels=Types_of_Homes, autopct='%1.1f%%', startangle=90,
        textprops={'rotation': 0, 'horizontalalignment': 'center', 'verticalalignment': 'center', 'wrap': True})
ax1.set_title("Distribution of Home Types in the United States, 2023")
ax1.axis('equal')

plt.tight_layout()
plt.savefig('pie chart/png/117.png')
plt.clf()
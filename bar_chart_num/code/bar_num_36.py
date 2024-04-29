
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))

Country = ['USA', 'UK', 'Germany', 'France']
Restaurants = [800, 500, 700, 600]
Grocery_Stores = [9000, 7000, 8000, 9000]
Takeaway = [600, 400, 500, 700]

x = np.arange(len(Country))
width = 0.2

ax = plt.subplot()
ax.bar(x - width, Restaurants, width=width, label='Restaurants')
ax.bar(x, Grocery_Stores, width=width, label='Grocery Stores')
ax.bar(x + width, Takeaway, width=width, label='Takeaway')

ax.set_ylabel('Number of Outlets')
ax.set_title('Number of food outlets in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()

for i, v in enumerate(Restaurants):
    ax.text(x[i] - width/2, v + 50, str(v), ha='center', va='bottom', rotation=0, fontsize=12)

for i, v in enumerate(Grocery_Stores):
    ax.text(x[i] + width/2, v + 50, str(v), ha='center', va='bottom', rotation=0, fontsize=12)

for i, v in enumerate(Takeaway):
    ax.text(x[i], v + 50, str(v), ha='center', va='bottom', rotation=0, fontsize=12)

plt.tight_layout()
plt.savefig('Bar Chart/png/159.png')
plt.clf()

import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
ax = plt.subplot()

month = ["January", "February", "March", "April", "May"]
inventory_A = [500, 600, 800, 1000, 1200]
inventory_B = [600, 800, 1000, 1200, 1400]
inventory_C = [800, 1000, 1200, 1400, 1600]
inventory_D = [900, 1100, 1400, 1600, 1800]

ax.plot(month, inventory_A, color='r', label='Inventory A')
ax.plot(month, inventory_B, color='b', label='Inventory B')
ax.plot(month, inventory_C, color='g', label='Inventory C')
ax.plot(month, inventory_D, color='y', label='Inventory D')

ax.set_xticks(month)
plt.title("Inventory Levels of Four Different Products in 2021")
ax.legend()
plt.tight_layout()
plt.savefig('line chart/png/374.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

month = np.arange(1, 6)
cars_sold = np.array([2.5, 2.3, 2.7, 3.1, 3.3])
cars_produced = np.array([2.7, 2.9, 3.1, 3.3, 3.5])
trucks_sold = np.array([1.2, 1.3, 1.6, 1.7, 1.9])
trucks_produced = np.array([1.4, 1.5, 1.8, 2.0, 2.2])

plt.plot(month, cars_sold, 'r', label='Cars Sold (millions)')
plt.plot(month, cars_produced, 'b', label='Cars Produced (millions)')
plt.plot(month, trucks_sold, 'g', label='Trucks Sold (millions)')
plt.plot(month, trucks_produced, 'y', label='Trucks Produced (millions)')

plt.xticks(month, ['Jan', 'Feb', 'Mar', 'Apr', 'May'], rotation=45, fontsize=10)

plt.title('Global Vehicle Production and Sales in 2020')
plt.xlabel('Month')
plt.ylabel('Quantity (millions)')
plt.grid(True)
plt.legend()

for a, b in zip(month, cars_sold):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=9)
for a, b in zip(month, cars_produced):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=9)
for a, b in zip(month, trucks_sold):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=9)
for a, b in zip(month, trucks_produced):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('line chart/png/94.png')
plt.clf()
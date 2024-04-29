
import matplotlib.pyplot as plt

year = [2020, 2021, 2022, 2023, 2024]
produce_price = [2.5, 2.7, 2.9, 2.6, 2.8]
dairy_price = [3.5, 3.6, 3.7, 3.8, 3.9]
meat_price = [4.5, 4.3, 4.1, 4.2, 4.0]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

ax.plot(year, produce_price, label="Produce", linewidth=1.5, color='#006699')
ax.plot(year, dairy_price, label="Dairy", linewidth=1.5, color='#F18F01')
ax.plot(year, meat_price, label="Meat", linewidth=1.5, color='#CC3300')

ax.grid(color='#CFCFCF', linestyle='--', linewidth=0.5)
ax.set_title("Average Price of Produce, Dairy and Meat from 2020 to 2024 in the Food and Beverage Industry", fontsize=14)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Price (Dollars)', fontsize=12)
ax.set_xticks(year)
ax.legend(loc="upper center", fontsize=10, bbox_to_anchor=(0.5, 1.1))

for a, b in zip(year, produce_price):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10, rotation=0)
for a, b in zip(year, dairy_price):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10, rotation=0)
for a, b in zip(year, meat_price):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10, rotation=0)

plt.tight_layout()
plt.savefig('line chart/png/257.png')
plt.clf()
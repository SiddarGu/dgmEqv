
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

year = [2001, 2002, 2003, 2004, 2005]
fast_food_costs = [5, 6, 7, 8, 9]
grocery_store_costs = [10, 11, 12, 13, 14]

ax.plot(year, fast_food_costs, label='Fast Food Costs', color='b', marker='o')
ax.plot(year, grocery_store_costs, label='Grocery Store Costs', color='r', marker='o')

for x, y in zip(year, fast_food_costs):
    ax.text(x, y + 0.2, y, ha='center', va='bottom', fontsize=10)
for x, y in zip(year, grocery_store_costs):
    ax.text(x, y + 0.2, y, ha='center', va='bottom', fontsize=10)

plt.title('Costs of Fast Food and Grocery Store Items from 2001 to 2005')
plt.xticks(year)
plt.xlabel('Year')
plt.ylabel('Costs (Dollars)')
plt.tight_layout()
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

plt.savefig('line chart/png/166.png')
plt.clf()
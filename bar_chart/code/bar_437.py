
import matplotlib.pyplot as plt

country = ['USA', 'Canada', 'UK', 'China']
Food = [100, 90, 80, 110]
Drink = [200, 190, 180, 220]

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()
ax.bar(country, Food, bottom=Drink, label='Food')
ax.bar(country, Drink, label='Drink')
ax.legend()
plt.title('Food and drink production in four countries in 2021', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar chart/png/376.png')
plt.clf()
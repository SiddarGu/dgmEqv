

import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

x = [2018, 2019, 2020, 2021]
y1 = [50, 70, 90, 110]
y2 = [60, 80, 100, 120]
y3 = [40, 50, 60, 70]

plt.plot(x, y1, label='Beverage A')
plt.plot(x, y2, label='Beverage B')
plt.plot(x, y3, label='Beverage C')

plt.xticks(x)
plt.title('Beverage sales in the food and beverage industry from 2018 to 2021')
plt.xlabel('Year')
plt.ylabel('Sales(tons)')
plt.legend()

plt.tight_layout()
plt.savefig('line chart/png/217.png')
plt.clf()
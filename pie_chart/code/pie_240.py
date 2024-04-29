
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7,7))
investment = ['Stocks', 'Bonds', 'Mutual Funds', 'ETFs', 'Money Market Funds']
percentage = [30, 30, 20, 10, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
explode = [0.1, 0, 0, 0, 0]

plt.title('Investment Portfolio Distribution in the USA, 2023')
plt.pie(percentage, colors = colors, labels=investment, autopct='%.2f%%', pctdistance=0.7, explode=explode, shadow=True, startangle=90)
plt.axis('equal')
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig('pie chart/png/263.png')
plt.clf()
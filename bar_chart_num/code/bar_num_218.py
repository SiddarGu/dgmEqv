
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

Country = ['USA', 'UK', 'Germany', 'France']
Agricultural_Products = [5000, 4000, 3000, 3500]
Food_Supply = [8000, 7000, 6000, 6500]

x = np.arange(len(Country))

plt.bar(x, Agricultural_Products, bottom=Food_Supply, align='center', label='Agricultural Products')
plt.bar(x, Food_Supply, align='center', label='Food Supply')

for x1, y1, y2 in zip(x, Food_Supply, Agricultural_Products):
    plt.annotate("{:.0f}".format(y1), xy=(x1, y1 / 2), color='black', ha='center')
    plt.annotate("{:.0f}".format(y2), xy=(x1, y1 + y2 / 2), color='black', ha='center')

plt.title("Agricultural production and food supply in four countries in 2021")
plt.xticks(x, Country)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('Bar Chart/png/31.png')
plt.clf()
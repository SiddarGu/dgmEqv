
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(1, 1, 1)

data = [['USA', 200, 800, 100],
        ['UK', 210, 750, 90],
        ['Germany', 220, 700, 80],
        ['France', 230, 650, 70]]

labels = ['Fast Food Restaurants', 'Grocery Stores', 'Cafes']
bottom = [0, 0, 0]

for i in range(3):
    ax.bar(data[i][0], data[i][i+1], label=labels[i], bottom=bottom[i])
    bottom[i] += data[i][i+1]

plt.xticks(data[i][0])
plt.title('Number of establishments in the food and beverage industry in four countries in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/415.png')

plt.clf()
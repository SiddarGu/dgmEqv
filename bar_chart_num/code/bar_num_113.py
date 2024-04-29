
import matplotlib.pyplot as plt
import numpy as np

category = ['USA', 'UK', 'Germany', 'France']
coffee = [500, 450, 400, 350]
tea = [300, 280, 260, 240]
rice = [1000, 900, 800, 700]

x = np.arange(len(category))
width = 0.2

fig, ax = plt.subplots(figsize=(10,7))
ax.bar(x, coffee, width, label='Coffee')
ax.bar(x + width, tea, width, label='Tea')
ax.bar(x + width*2, rice, width, label='Rice')

ax.set_title('Amount of coffee, tea and rice produced in four countries in 2021')
ax.set_xticks(x + width)
ax.set_xticklabels(category)
ax.legend()

for i in range(len(category)):
    ax.annotate(coffee[i], (x[i] - 0.1, coffee[i] + 10))
    ax.annotate(tea[i], (x[i] + 0.1, tea[i] + 10))
    ax.annotate(rice[i], (x[i] + 0.3, rice[i] + 10))

plt.tight_layout()
plt.savefig('Bar Chart/png/171.png')
plt.clf()
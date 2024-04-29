
import matplotlib.pyplot as plt
import numpy as np

data = [[3000, 2500, 2000], [4000, 3500, 2500], [3500, 3000, 2000], [3000, 2800, 4000]]
countries = ['USA', 'UK', 'Germany', 'France']
wheat = [x[0] for x in data]
rice = [x[1] for x in data]
corn = [x[2] for x in data]

fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot()
p1 = ax.bar(countries, wheat, label='Wheat Production(tons)', bottom=0, width=0.2)
p2 = ax.bar(countries, rice, label='Rice Production(tons)', bottom=wheat, width=0.2)
p3 = ax.bar(countries, corn, label='Corn Production(tons)', bottom=[sum(x) for x in zip(wheat, rice)], width=0.2)
ax.set_title('Grain production in four countries in 2021')
ax.grid(linestyle='--')
ax.legend(loc='upper left')
plt.xticks(rotation=90)
for x, y in zip(countries, data):
    ax.annotate(str(y), xy=(x, sum(y)), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom', fontsize=12)
plt.tight_layout()
plt.savefig('Bar Chart/png/601.png')
plt.clf()
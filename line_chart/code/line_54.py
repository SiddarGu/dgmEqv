
import matplotlib.pyplot as plt
import numpy as np

data = [[2019,5000,3000,4000,7000],
        [2020,5500,2500,4500,8000],
        [2021,6000,3000,5000,9000],
        [2022,7000,3500,6000,10000]]

data = np.array(data)

x = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]
y3 = data[:, 3]
y4 = data[:, 4]

plt.figure(figsize=(12, 8))
ax = plt.subplot()
ax.plot(x, y1, label="Cereal(tonnes)", marker='o', linestyle='--')
ax.plot(x, y2, label="Bakery(tonnes)", marker='o', linestyle='-.')
ax.plot(x, y3, label="Canned Food(tonnes)", marker='o', linestyle=':')
ax.plot(x, y4, label="Frozen Food(tonnes)", marker='o', linestyle='-')
plt.title("Global Food Production Trends in the Food and Beverage Industry")
ax.set_xticks(x)
plt.xlabel("Year")
plt.ylabel("Tonnes")
plt.legend(loc='best', bbox_to_anchor=(1, 0.8))
plt.tight_layout()
plt.savefig('line chart/png/410.png')
plt.clf()
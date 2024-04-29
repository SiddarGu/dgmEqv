
import matplotlib.pyplot as plt
import numpy as np

data = [['Asia', 20000, 30000],
        ['Europe', 25000, 35000],
        ['North America', 22000, 32000],
        ['South America', 19000, 27000]]

x_name = [i[0] for i in data]
y_renewable = [i[1] for i in data]
y_non_renewable = [i[2] for i in data]

x_pos = np.arange(len(x_name))

plt.figure(figsize=(10,6))

ax = plt.subplot()

ax.bar(x_pos, y_renewable, width=0.4, label='Renewable Energy (MWh)', color='green')
ax.bar(x_pos, y_non_renewable, width=0.4, label='Non-Renewable Energy (MWh)', bottom=y_renewable, color='orange')

ax.set_xticks(x_pos)
ax.set_xticklabels(x_name, rotation=90, wrap=True)
ax.set_ylabel('MWh')
ax.set_title('Comparison of Renewable and Non-Renewable Energy Consumption in Four Regions in 2021')
ax.legend()

for x, y_renewable, y_non_renewable in zip(x_pos, y_renewable, y_non_renewable):
    ax.text(x, y_renewable/2, y_renewable, ha='center', va='bottom', fontsize=10)
    ax.text(x, y_renewable+y_non_renewable/2, y_non_renewable, ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('Bar Chart/png/553.png')
plt.clf()
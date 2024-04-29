
import matplotlib.pyplot as plt
import numpy as np

data = [[2018, 65, 100], [2019, 70, 200], [2020, 73, 400], [2021, 75, 450], [2022, 77, 500]]

x = [row[0] for row in data]
y1 = [row[1] for row in data]
y2 = [row[2] for row in data]

plt.figure(figsize=(12, 8))
ax = plt.subplot()
ax.plot(x, y1, color='#E41A1C', marker='o', label='Voter Turnout(percentage)')
ax.plot(x, y2, color='#377EB8', marker='o', label='Campaign Expenditure(million dollars)')

ax.set_xticks(x)
ax.set_xticklabels(x, rotation=0, fontsize=14)
ax.set_yticks(np.arange(0, 100, 10))

ax.set_title('Effect of Campaign Expenditure on Voter Turnout in the USA from 2018 to 2022', fontsize=18)
ax.legend(loc='upper left', fontsize=14)

plt.tight_layout()
plt.savefig('line chart/png/134.png')
plt.clf()
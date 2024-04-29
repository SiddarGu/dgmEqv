
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(16, 6))

year = [2018,2019,2020,2021,2022]
computers = [50,60,70,80,90]
phones = [300,350,400,420,450]
games = [20,25,30,35,40]

plt.plot(year, computers, linestyle='-', marker='o', color='b', label='Computer Sales (million units)')
plt.plot(year, phones, linestyle='-', marker='o', color='r', label='Phone Sales (million units)')
plt.plot(year, games, linestyle='-', marker='o', color='g', label='Games Console Sales (million units)')

plt.xticks(np.arange(min(year), max(year)+1, 1.0))

plt.xlabel('Year')
plt.ylabel('Sales (million units)')
plt.title('Global Technology Sales from 2018 to 2022')
plt.legend(loc='upper left')

for a,b,c,d in zip(year, computers, phones, games): 
    plt.annotate('{}, {}, {}'.format(b,c,d), xy=(a, b), xytext=(a-0.15, b+1),
            fontsize=10,
            bbox=dict(boxstyle="round", fc="0.8"))

plt.tight_layout()
plt.savefig('line chart/png/120.png')
plt.clf()
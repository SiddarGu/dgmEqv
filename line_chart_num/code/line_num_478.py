
import matplotlib.pyplot as plt

month = ['January', 'February', 'March', 'April', 'May']
a = [3000, 3500, 2500, 3000, 3500]
b = [1500, 1700, 1500, 2000, 2200]
c = [2500, 2800, 3000, 3500, 4000]
d = [2000, 2200, 1800, 2200, 2500]

plt.figure(figsize=(10, 6))
plt.plot(month, a, label = 'Production A', marker='o')
plt.plot(month, b, label = 'Production B', marker='o')
plt.plot(month, c, label = 'Production C', marker='o')
plt.plot(month, d, label = 'Production D', marker='o')
plt.xticks(month, rotation = 'vertical')
plt.title('Monthly production of four products in 2021', fontsize=15)
plt.xlabel('Month')
plt.ylabel('Production (units)')
plt.legend()
plt.grid(linestyle='-.')

for x, y in zip(month, a):
    plt.annotate(y, xy=(x, y), xytext=(0, 10), 
        textcoords='offset points', ha='center')

for x, y in zip(month, b):
    plt.annotate(y, xy=(x, y), xytext=(0, 10), 
        textcoords='offset points', ha='center')

for x, y in zip(month, c):
    plt.annotate(y, xy=(x, y), xytext=(0, 10), 
        textcoords='offset points', ha='center')

for x, y in zip(month, d):
    plt.annotate(y, xy=(x, y), xytext=(0, 10), 
        textcoords='offset points', ha='center')

plt.tight_layout()
plt.savefig('line chart/png/135.png')
plt.clf()
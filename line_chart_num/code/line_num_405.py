
import matplotlib.pyplot as plt

x = ['January', 'February', 'March', 'April']
y1 = [2000, 2500, 3000, 3500]
y2 = [500, 600, 700, 800]
y3 = [1000, 1100, 1200, 1300]
y4 = [3000, 2500, 1500, 1000]

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Solar Energy(KWh)', color='green', marker='o', linestyle='dashed', linewidth=2, markersize=6)
plt.plot(x, y2, label='Wind Energy(KWh)', color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=6)
plt.plot(x, y3, label='Hydro Energy(KWh)', color='red', marker='o', linestyle='dashed', linewidth=2, markersize=6)
plt.plot(x, y4, label='Nuclear Energy(KWh)', color='orange', marker='o', linestyle='dashed', linewidth=2, markersize=6)

plt.xlabel('Month')
plt.ylabel('KWh')
plt.title('Energy Production in Four Sources in the U.S. from January to April 2021')
plt.xticks(x)
plt.legend()

for x, y1, y2, y3, y4 in zip(x, y1, y2, y3, y4):
    plt.annotate(str(y1), xy=(x, y1), xytext=(-15, 10), textcoords='offset points')
    plt.annotate(str(y2), xy=(x, y2), xytext=(-15, 10), textcoords='offset points')
    plt.annotate(str(y3), xy=(x, y3), xytext=(-15, 10), textcoords='offset points')
    plt.annotate(str(y4), xy=(x, y4), xytext=(-15, 10), textcoords='offset points')

plt.tight_layout()
plt.savefig('line chart/png/84.png', dpi=300)
plt.clf()
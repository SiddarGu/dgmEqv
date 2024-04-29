
import matplotlib.pyplot as plt
import numpy as np

months = ["January", "February", "March", "April", "May"]
production_A = [500, 600, 700, 800, 900]
production_B = [800, 700, 900, 1000, 1200]
production_C = [1000, 1100, 1300, 1500, 1800]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.plot(months, production_A, marker='o', linestyle='-', color='blue', label='Production A')
ax.plot(months, production_B, marker='o', linestyle='-', color='red', label='Production B')
ax.plot(months, production_C, marker='o', linestyle='-', color='green', label='Production C')
ax.legend(loc='upper left', fontsize='large')

for x, y in zip(months, production_A):
    ax.annotate(str(y), xy=(x,y), xytext=(-5, 5), textcoords='offset points')
for x, y in zip(months, production_B):
    ax.annotate(str(y), xy=(x,y), xytext=(-5, 5), textcoords='offset points')
for x, y in zip(months, production_C):
    ax.annotate(str(y), xy=(x,y), xytext=(-5, 5), textcoords='offset points')

plt.xticks(np.arange(len(months)), months, rotation=45)
plt.title("Production of three items in a factory in 2020")
plt.tight_layout()
plt.savefig("line chart/png/220.png")
plt.clf()


import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(14,6))

month = ["January", "February", "March", "April", "May"]
movies = [25, 20, 19, 22, 27]
concerts = [15, 17, 20, 18, 23]
exhibitions = [10, 12, 14, 16, 19]

x = np.arange(len(month))

plt.plot(x, movies, label="Movies Released")
plt.plot(x, concerts, label="Concerts")
plt.plot(x, exhibitions, label="Art Exhibitions")

plt.xticks(x, month, rotation=45, wrap=True)

for xpos, ypos, yval in zip(x, movies, movies):
     plt.text(xpos, ypos, yval, fontsize=12, horizontalalignment='center')

for xpos, ypos, yval in zip(x, concerts, concerts):
     plt.text(xpos, ypos, yval, fontsize=12, horizontalalignment='center')

for xpos, ypos, yval in zip(x, exhibitions, exhibitions):
     plt.text(xpos, ypos, yval, fontsize=12, horizontalalignment='center')

plt.title('Monthy Arts and Culture Events in 2021')
plt.xlabel("Month")
plt.ylabel("Number of Events")
plt.legend(loc="upper right")
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/103.png')
plt.clf()
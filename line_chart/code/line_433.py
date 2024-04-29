
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2001, 2002, 2003, 2004])
movies = np.array([50, 60, 80, 90])
music = np.array([60, 55, 65, 75])
art = np.array([70, 80, 90, 100])

fig, ax = plt.subplots(figsize=(10,8))
plt.plot(x, movies, label='Movies')
plt.plot(x, music, label='Music')
plt.plot(x, art, label='Art')

plt.xticks(x)
plt.title("Popularity of Arts in the US from 2001 to 2004")
plt.xlabel("Year")
plt.ylabel("Popularity")
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.savefig("line chart/png/32.png")
plt.clf()
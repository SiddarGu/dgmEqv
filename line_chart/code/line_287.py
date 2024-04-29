
import matplotlib.pyplot as plt
import numpy as np

year = [2001, 2002, 2003, 2004]
production_A = [100, 150, 200, 250]
production_B = [200, 250, 300, 350]
production_C = [300, 350, 400, 450]
production_D = [400, 450, 500, 550]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

ax.plot(year, production_A, color='blue', label="Production A")
ax.plot(year, production_B, color='green', label="Production B")
ax.plot(year, production_C, color='red', label="Production C")
ax.plot(year, production_D, color='black', label="Production D")

ax.set_xticks(np.arange(2001, 2005, 1))
ax.set_xlabel("Year")
ax.set_ylabel("Units")
ax.set_title("Manufacturing Output of Four Product Types from 2001-2004")

ax.legend(loc="best")

plt.tight_layout()

plt.savefig("line chart/png/504.png")
plt.clf()
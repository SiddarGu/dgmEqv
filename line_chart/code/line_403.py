
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6), dpi=120)

x = np.arange(6)
y1 = [6.1, 6.2, 6.4, 6.6, 6.8, 7.0]
y2 = [67, 68, 69, 70, 71, 72]
y3 = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7]

plt.plot(x, y1, label="Population(millions)")
plt.plot(x, y2, label="Life Expectancy(years)")
plt.plot(x, y3, label="GDP(trillion dollars)")

plt.title("Global population, life expectancy and GDP growth from 2000 to 2005")
plt.xlabel("Year")
plt.ylabel("Number")
plt.xticks(x, ["2000", "2001", "2002", "2003", "2004", "2005"])
plt.legend()

plt.grid(True, linestyle="--", color="gray", linewidth="1", alpha=0.5)
plt.tight_layout()
plt.savefig("line chart/png/395.png")

plt.close()

import matplotlib.pyplot as plt
import numpy as np

year = [2001,2002,2003,2004,2005,2006,2007]
gdp = np.array([1000,1200,800,1500,1600,900,1300])
debt = np.array([100,200,300,400,500,600,700])

fig, ax = plt.subplots(figsize=(10,6))
ax.plot(year, gdp, label="GDP (billion dollars)", color="green")
ax.plot(year, debt, label="Debt (billion dollars)", color="blue")
ax.legend()
ax.set_title("GDP and Debt Growth in the United States from 2001 to 2007")
ax.set_xticks(year)
ax.set_xlabel("Year")
ax.set_ylabel("GDP and Debt (billion dollars)")
plt.tight_layout()
plt.savefig("line chart/png/162.png")
plt.clf()
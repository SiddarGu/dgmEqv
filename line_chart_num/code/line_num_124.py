
import matplotlib.pyplot as plt
import numpy as np

Year = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030])
E_commerce = np.array([3, 15, 30, 50, 70, 85, 97])
Retail = np.array([97, 85, 70, 50, 30, 15, 3])

plt.figure(figsize=(18,10))
ax = plt.subplot()

ax.plot(Year, E_commerce, color='purple', label='E-commerce')
ax.plot(Year, Retail, color='green', label='Retail')

ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage(%)", fontsize=12)
ax.set_title("The Growing Trend of E-commerce in the Last Decade", fontsize=14)

ax.xaxis.set_ticks(Year)

for i,j in zip(Year, E_commerce):
    ax.annotate(str(j),xy=(i,j+1))
for i,j in zip(Year, Retail):
    ax.annotate(str(j),xy=(i,j+1))

ax.grid(True, linestyle='--', linewidth=1, color='black', alpha=.3)
ax.legend(loc='lower right')

plt.savefig("line chart/png/272.png")
plt.tight_layout()
plt.clf()
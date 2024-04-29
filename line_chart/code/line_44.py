
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,13)
y1 = [25,27,30,35,40,45,50,55,50,45,40,35]
y2 = [700,800,850,950,1000,1100,1200,1300,1200,1100,1000,950]
y3 = [500,550,600,650,700,800,850,950,850,800,700,650]

plt.figure(figsize=(14,7))
plt.plot(x, y1, label="Visitors (thousands)")
plt.plot(x, y2, label="Hotel Revenue (million dollars)")
plt.plot(x, y3, label="Restaurant Revenue (million dollars)")
plt.xticks(x)
plt.title("Tourist visits and revenue of the hospitality industry in London in 2021")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend(loc=2, prop={'size': 10, 'family': 'serif'})
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/150.png')
plt.clf()
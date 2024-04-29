
import matplotlib.pyplot as plt
import numpy as np

# Prepare data
data = [[2001,500,600], [2002,550,620], [2003,650,720], [2004,700,800], [2005,750,850]]
year, retail, wholesale = np.transpose(data)

# Plot figure
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
ax.plot(year, retail, label='Retail Sales')
ax.plot(year, wholesale, label='Wholesale Sales')
ax.set_title('Retail and Wholesale Sales in the US from 2001 to 2005')
ax.set_xlabel('Year')
ax.set_ylabel('Sales (billion dollars)')
ax.legend(loc='upper left')
ax.grid(True)
ax.set_xticks(year)
ax.annotate('Max Retail Sales', xy=(2004, 700), xytext=(2003, 650),arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Max Wholesale Sales', xy=(2005, 850), xytext=(2004, 800),arrowprops=dict(facecolor='black', shrink=0.05))
plt.tight_layout()
plt.savefig('line chart/png/181.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

data = [[2019,400,50],[2020,420,48],[2021,430,45],[2022,440,43],[2023,460,40],[2024,480,38]]

x, y1, y2 = np.array(data).T

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(x, y1, color = 'red', marker='o', label='CO2 Emission')
ax.plot(x, y2, color = 'blue', marker='o', label='Ozone Levels')

ax.set_title('Global CO2 Emission and Ozone Levels from 2019 to 2024')
ax.set_xlabel('Year')
ax.set_ylabel('Levels')
ax.legend(loc="lower right")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xticks(x)
ax.grid(True)
plt.tight_layout()

plt.savefig('line chart/png/84.png')
plt.clf()
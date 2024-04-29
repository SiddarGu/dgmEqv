
import matplotlib.pyplot as plt
import numpy as np

year = [2015, 2016, 2017, 2018, 2019]
Painting_A = [3000, 3500, 4000, 4500, 3500]
Painting_B = [4000, 4500, 5000, 4000, 4500]
Painting_C = [2500, 3000, 3500, 4000, 3000]
Painting_D = [3000, 3500, 4000, 4500, 3500]

fig = plt.figure(figsize = (10, 6))
ax = fig.add_subplot(111)
ax.plot(year, Painting_A, label='Painting A')
ax.plot(year, Painting_B, label='Painting B')
ax.plot(year, Painting_C, label='Painting C')
ax.plot(year, Painting_D, label='Painting D')
ax.set_xlabel('Year')
ax.set_ylabel('Prices')
ax.set_title('Prices of four paintings over the last 5 years')
plt.xticks(year)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('line chart/png/213.png')
plt.clf()


import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,8))

x = np.arange(2000, 2005, 1)
y1 = [25, 24, 25, 23, 24]
y2 = [12, 11, 12, 10, 11]
y3 = [80, 81, 79, 82, 81]

plt.plot(x, y1, label='Birth Rate(per 1000)', color='red', linewidth=2)
plt.plot(x, y2, label='Death Rate(per 1000)', color='green', linewidth=2)
plt.plot(x, y3, label='Life Expectancy', color='blue', linewidth=2)
plt.xticks(x)
plt.title('Trends in birth rate, death rate, and life expectancy in the United States from 2000-2004')
plt.xlabel('Year')
plt.ylabel('Rate')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/307.png')
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))

year = [1950, 1960, 1970, 1980]
painting_A = [1000, 1200, 800, 1500]
painting_B = [800, 900, 1100, 1200]
painting_C = [1200, 1100, 1300, 1400]
painting_D = [1500, 1600, 1200, 800]

plt.plot(year, painting_A, label='Painting A', color='red', marker='o')
plt.plot(year, painting_B, label='Painting B', color='gold', marker='o')
plt.plot(year, painting_C, label='Painting C', color='blue', marker='o')
plt.plot(year, painting_D, label='Painting D', color='green', marker='o')

plt.xticks(year)
plt.title('Price of Paintings in the Art Market from 1950 to 1980')
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.legend(loc='best')

for x, y in zip(year, painting_A):
    plt.annotate(y, xy=(x, y), xytext=(x+0.2, y+100), fontsize=8)
    
for x, y in zip(year, painting_B):
    plt.annotate(y, xy=(x, y), xytext=(x+0.2, y+100), fontsize=8)
    
for x, y in zip(year, painting_C):
    plt.annotate(y, xy=(x, y), xytext=(x+0.2, y+100), fontsize=8)
    
for x, y in zip(year, painting_D):
    plt.annotate(y, xy=(x, y), xytext=(x+0.2, y+100), fontsize=8)

plt.tight_layout()
plt.savefig('line chart/png/24.png', dpi=300)
plt.clf()
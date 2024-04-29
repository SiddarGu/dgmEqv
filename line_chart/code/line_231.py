
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.set_title('Comparison of Box Office and Ticket Sales in the Entertainment Industry from 2020 to 2024')
ax.set_xlabel('Year')
ax.set_ylabel('Amount (million dollars)')

x = [2020, 2021, 2022, 2023, 2024]
y1 = [7000, 8000, 9000, 10000, 11000]
y2 = [1000, 2000, 3000, 4000, 5000]

ax.plot(x, y1, color='red', label='Box Office')
ax.plot(x, y2, color='blue', label='Ticket Sales')

plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/321.png')
plt.clf()
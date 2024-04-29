
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 6))
ax = plt.subplot()

years = np.array([2017, 2018, 2019, 2020])
A = np.array([1000, 1200, 1400, 1500])
B = np.array([700, 1000, 900, 1100])
C = np.array([500, 800, 600, 900])

plt.plot(years, A, label='Exhibition A Visitors')
plt.plot(years, B, label='Exhibition B Visitors')
plt.plot(years, C, label='Exhibition C Visitors')

plt.xticks(years)
plt.title('Visitor trend of three exhibitions in the past four years')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Years')
plt.ylabel('Visitors')

for a, b, c in zip(years, A, B):
    ax.annotate(str(b), xy=(a, b))
    ax.annotate(str(c), xy=(a, c))

plt.tight_layout()
plt.savefig('line chart/png/559.png')
plt.clf()
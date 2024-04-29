
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 8))
plt.title('Test scores of 5th to 10th graders in a school')

x = np.array([5, 6, 7, 8, 9, 10])
y1 = np.array([80, 85, 90, 95, 100, 95])
y2 = np.array([75, 85, 90, 95, 100, 95])
y3 = np.array([90, 85, 90, 95, 100, 95])

plt.plot(x, y1, marker='o', markersize=8, linestyle='--', linewidth=2, label='Test Score A')
plt.plot(x, y2, marker='s', markersize=8, linestyle='-.', linewidth=2, label='Test Score B')
plt.plot(x, y3, marker='*', markersize=8, linestyle=':', linewidth=2, label='Test Score C')

plt.xticks(x)
for i, j in zip(x, y1):
    plt.annotate(str(j), xy=(i, j+2))
for i, j in zip(x, y2):
    plt.annotate(str(j), xy=(i, j+2))
for i, j in zip(x, y3):
    plt.annotate(str(j), xy=(i, j+2))

plt.legend(loc='lower right')  
plt.grid(True, linestyle='--', linewidth=1, color='gray', axis='x', alpha=0.5)
plt.tight_layout()
plt.savefig('line chart/png/15.png')
plt.clf()
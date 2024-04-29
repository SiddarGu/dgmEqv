
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
math = np.array([90,92,94,96,98])
english = np.array([80,81,83,85,87])
science = np.array([85,87,89,91,93])

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, math, marker='o', color='blue', label='Math')
ax.plot(x, english, marker='o', color='red', label='English')
ax.plot(x, science, marker='o', color='green', label='Science')
ax.grid(linestyle='--', linewidth=1, alpha=0.5)
plt.xlabel('Grade', fontsize=14)
plt.ylabel('Average Score', fontsize=14)
plt.xticks(x)
plt.title('Average Score of Math, English, and Science in Elementary School', fontsize=14)
for a, b, c, d in zip(x, math, english, science):
    ax.text(a-0.08, b+0.2, b, ha='center', va='bottom', fontsize=10)
    ax.text(a-0.08, c+0.2, c, ha='center', va='bottom', fontsize=10)
    ax.text(a-0.08, d+0.2, d, ha='center', va='bottom', fontsize=10)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/499.png')
plt.clf()
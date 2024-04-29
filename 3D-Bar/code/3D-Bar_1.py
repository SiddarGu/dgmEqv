
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Number of Employees", "Average Working Hours", "Total Productivity (Units)"]
x_values = ["North", "South", "East", "West"]
data = np.array([[1000, 4000, 4500], 
              [900, 4500, 4000], 
              [1200, 3500, 4200], 
              [1100, 3800, 4600]])

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [0] * len(x_values), 0.5, 0.5, data[:, i], shade=True, alpha=0.7, label=y_values[i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Manufacturing and Production Analysis by Region')
plt.tight_layout()
plt.show()
plt.clf()
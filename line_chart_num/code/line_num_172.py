
import matplotlib.pyplot as plt
import numpy as np

Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
Pneumonia_Cases = [10, 15, 20, 25, 30, 35]
Colds_Cases = [25, 30, 35, 40, 45, 50]
Influenza_Cases = [20, 25, 30, 35, 40, 45]

fig, ax = plt.subplots(figsize=(14,7))
ax.plot(Month, Pneumonia_Cases, label="Pneumonia Cases", color='red', linestyle='dashed', marker='o', markerfacecolor='black', markersize=7)
ax.plot(Month, Colds_Cases, label="Colds Cases", color='blue', linestyle='dashed', marker='o', markerfacecolor='black', markersize=7)
ax.plot(Month, Influenza_Cases, label="Influenza Cases", color='green', linestyle='dashed', marker='o', markerfacecolor='black', markersize=7)

ax.set_title('Monthly cases of Pneumonia, Colds and Influenza in 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Cases')
ax.legend()

for a, b in zip(Month, Pneumonia_Cases):
    ax.annotate(str(b), xy=(a, b), fontsize=15)

for a, b in zip(Month, Colds_Cases):
    ax.annotate(str(b), xy=(a, b), fontsize=15)

for a, b in zip(Month, Influenza_Cases):
    ax.annotate(str(b), xy=(a, b), fontsize=15)

plt.xticks(Month)
plt.tight_layout()
plt.savefig('line chart/png/354.png')
plt.clf()
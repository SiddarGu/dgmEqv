
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1000, 1500, 2000], [900, 1600, 1700], [1100, 1300, 1900], [1200, 1400, 1800]])
Month = np.array(['January', 'February', 'March', 'April'])

fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(Month, data[:, 0], marker='o', label='Hospital A(patients)')
ax.plot(Month, data[:, 1], marker='x', label='Hospital B(patients)')
ax.plot(Month, data[:, 2], marker='s', label='Hospital C(patients)')

ax.set_xticks(Month)
ax.set_title('Monthly patient visits at three hospitals in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Number of patients')
ax.grid(True)
ax.legend(loc='best')

for i in range(4):
    ax.annotate(data[i], (Month[i], data[i][0]))
    ax.annotate(data[i], (Month[i], data[i][1]))
    ax.annotate(data[i], (Month[i], data[i][2]))

plt.tight_layout()
plt.savefig('line chart/png/548.png')
plt.clf()
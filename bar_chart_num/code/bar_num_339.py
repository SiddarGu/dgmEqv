
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

data = [[0, 400, 1000],
        [1, 400, 800],
        [2, 700, 1200],
        [3, 1000, 1500],
        [4, 900, 1300],
        [5, 500, 1100]]

age_group = [d[0] for d in data]
visits = [d[1] for d in data]
tests = [d[2] for d in data]

x = np.arange(len(age_group))
width = 0.4

ax.bar(x-width/2, visits, width, label='Visits')
ax.bar(x+width/2, tests, width, label='Tests')

ax.set_xticks(x)
ax.set_xticklabels(age_group)
ax.set_title('Number of healthcare visits and tests by age group in 2021')
ax.legend()

for i, v in enumerate(visits):
    ax.text(x[i] - width/2, v + 10, str(v), fontsize=9, ha='center', va='bottom', rotation=90)

for i, t in enumerate(tests):
    ax.text(x[i] + width/2, t + 10, str(t), fontsize=9, ha='center', va='bottom', rotation=90)

fig.tight_layout()
plt.savefig('Bar Chart/png/268.png')
plt.clf()
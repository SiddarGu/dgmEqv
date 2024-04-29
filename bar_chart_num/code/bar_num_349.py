
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot()

region = ['North America', 'South America', 'Europe', 'Asia']
education = [100, 90, 110, 80]
healthcare = [120, 110, 130, 100]
housing = [130, 140, 150, 120]

bar_width = 0.2
x = np.arange(len(region))

ax.bar(x, education, bar_width, label='Education', color='#8ec5fc')
ax.bar(x + bar_width, healthcare, bar_width, label='Healthcare', color='#c7e9b4')
ax.bar(x + 2*bar_width, housing, bar_width, label='Housing', color='#ffa69e')

ax.set_title('Social services availability in four regions in 2021')
ax.set_xticks(x + bar_width)
ax.set_xticklabels(region)
ax.legend(loc='best')

for i in range(len(region)):
    ax.annotate(education[i], (x[i] - 0.15, education[i] + 0.5))
    ax.annotate(healthcare[i], (x[i] + 0.05, healthcare[i] + 0.5))
    ax.annotate(housing[i], (x[i] + 0.25, housing[i] + 0.5))

plt.tight_layout()
plt.savefig('Bar Chart/png/309.png')
plt.clf()
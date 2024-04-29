
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.set_title('Number of engineering and science research papers from 2018 to 2021')
Year = [2018,2019,2020,2021]
Engineering_Research_Paper = [5.3,6.2,7.1,8.0]
Science_Research_Paper = [4.4,5.2,6.4,7.2]
ax.bar(Year, Engineering_Research_Paper, width=0.3, label='Engineering Research Paper(million)', bottom=Science_Research_Paper)
ax.bar(Year, Science_Research_Paper, width=0.3, label='Science Research Paper(million)')
ax.set_xticks(Year)
ax.legend(loc='upper left')

for a, b, c in zip(Year, Engineering_Research_Paper, Science_Research_Paper):
    ax.annotate('%.1f' % b, xy=(a, b+0.2), ha='center')
    ax.annotate('%.1f' % c, xy=(a, c+0.2), ha='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/387.png')
plt.clf()
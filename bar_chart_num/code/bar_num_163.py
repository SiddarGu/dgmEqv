
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig = plt.figure()
ax = fig.add_subplot()

month = ['January', 'February', 'March', 'April']
online = [3000, 3500, 3700, 4000]
store = [2000, 2200, 2500, 2700]

pos = [i for i, _ in enumerate(month)]
ax.bar(pos, online, color='green', width=0.8, label='Online Sales')
ax.bar(pos, store, color='blue', width=0.8, label='Store Sales', bottom=online)

ax.set_xticks(pos)
ax.set_xticklabels(month)
ax.set_ylabel('Million')
ax.set_title('Comparison of online and store sales from January to April 2021')
ax.legend(loc='upper center')
ax.annotate('3000', xy=(0,3000))
ax.annotate('2000', xy=(0,2000))
ax.annotate('3500', xy=(1,3500))
ax.annotate('2200', xy=(1,2200))
ax.annotate('3700', xy=(2,3700))
ax.annotate('2500', xy=(2,2500))
ax.annotate('4000', xy=(3,4000))
ax.annotate('2700', xy=(3,2700))

plt.tight_layout()
fig.set_size_inches(8, 6)
plt.savefig('Bar Chart/png/66.png')
plt.clf()
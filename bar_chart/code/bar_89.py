
import matplotlib.pyplot as plt

y1 = [20000,25000,18000,23000]
y2 = [40000,45000,42000,47000]

x = ["USA", "UK", "Germany", "France"]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.bar(x, y1, width=0.3, label='High School Students', color='b')
ax.bar(x, y2, width=0.3, bottom=y1, label='University Students', color='r')

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),  shadow=True, ncol=2)
ax.set_title('Number of high school and university students in four countries in 2021')
ax.set_xticks(x)
plt.tight_layout()
plt.savefig('bar chart/png/71.png')
plt.clf()

import matplotlib.pyplot as plt

x = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
y1 = [50, 45, 40, 35, 43, 47, 50]
y2 = [70, 75, 80, 85, 78, 70, 65]

plt.figure(figsize=(10,6))
ax = plt.subplot()

ax.plot(x, y1, label='Average Air Quality Index', color='red', linewidth=2)
ax.plot(x, y2, label='Average Water Quality Index', color='green', linewidth=2)

for a, b in zip(x, y1):
    ax.annotate("{}".format(b), xy=(a, b), xytext=(a, b+5))
for c, d in zip(x, y2):
    ax.annotate("{}".format(d), xy=(c, d), xytext=(c, d+3))

ax.set_title("Air and Water Quality Index in the U.S. 2001-2007")
ax.set_xlabel("Year")
ax.set_ylabel("Index Value")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='lower right', frameon=False)
ax.set_xticks(x)
plt.tight_layout()

plt.savefig('line chart/png/406.png')

plt.clf()
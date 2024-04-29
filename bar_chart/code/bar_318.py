
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

x_labels = ["Air", "Sea", "Ground"]
cost = [10, 3, 2]
time = [3, 15, 7]

x = range(len(x_labels))
ax.bar(x, cost, label="Cost(thousand USD)", width=0.4, bottom=0)
ax.bar(x, time, label="Time(days)", width=0.4, bottom=cost, alpha=0.3)

ax.set_title("Cost and Time of Transportation by Different Modes in 2021")
ax.set_xticks(x)
ax.set_xticklabels(x_labels, rotation=90)
ax.legend(loc="best")
plt.tight_layout()
plt.savefig("bar_318.png")
plt.clf()
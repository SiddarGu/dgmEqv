
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
ax = plt.subplot()

x=('USA', 'UK', 'Germany', 'France')
y1=(100, 90, 80, 70)
y2=(200, 180, 160, 140)
y3=(50, 40, 30, 20)

ax.bar(x, y1, label="Museums", bottom=0, width=0.25, color="b")
ax.bar(x, y2, label="Galleries", bottom=y1, width=0.25, color="y")
ax.bar(x, y3, label="Cultural Centers", bottom=y2, width=0.25, color="g")

ax.set_title("Number of cultural attractions in four countries in 2021") 
ax.set_ylabel("Number of Attractions")
ax.set_xlabel("Country")

ax.legend(loc="upper right")

ax.set_xticks(x)
plt.tight_layout()

plt.savefig("bar chart/png/356.png")
plt.clf()
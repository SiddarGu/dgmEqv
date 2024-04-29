
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

devices = ["Desktops", "Laptops", "Tablets", "Smartphones"]
usage = [20, 30, 15, 35]

ax.pie(usage, labels=devices, autopct="%.2f%%", textprops={'fontsize': 14, 'wrap': True}, shadow=True, rotatelabels=True)
ax.set_title("Usage of Digital Devices in 2021", fontsize=20)

plt.tight_layout()
plt.xticks([])

plt.savefig("pie chart/png/131.png")
plt.clf()

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))
ax = plt.subplot()

events = ["Earthquake", "Tornado", "Hurricane", "Volcano eruption", "Avalanche"]
energy = [1000, 2200, 3000, 4000, 1200]

plt.plot(events, energy, color="purple", marker="o", linestyle="--")

plt.title("Energy released from different natural disasters")
ax.set_xlabel("Event")
ax.set_ylabel("Energy (joules)")
plt.xticks(rotation=45)
plt.xticks(events)

for a, b in zip(events, energy):
    plt.annotate(str(b), xy=(a, b), xytext=(0, 5),
                 textcoords="offset points",
                 fontsize=12, ha="center")

plt.tight_layout()
plt.savefig("line chart/png/381.png")
plt.clf()

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

sports = ["Football", "Basketball", "Baseball", "Hockey"]
participants = [30, 25, 20, 15]
spectators = [450, 400, 350, 300]

ax.bar(sports, participants, label="Participants", width=0.4, color='b', bottom=0)
ax.bar(sports, spectators, label="Spectators", width=0.4, color='g')

ax.set_title("Number of participants and spectators of four sports in 2021")
ax.set_xlabel("Sport")
ax.set_ylabel("Number")

ax.legend(loc="upper right")
ax.set_xticklabels(sports, rotation=45, ha='right', va='top', wrap=True)

fig.tight_layout()
plt.savefig("bar chart/png/46.png")
plt.clf()
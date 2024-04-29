
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()
ax.set_title("Sports and Entertainment Attendance and Tickets Sold in 2021")

Events = ["Football", "Basketball", "Hockey", "Volleyball"]
Attendees = [50, 65, 70, 60]
Tickets_Sold = [600, 750, 800, 700]

x_pos = [i for i, _ in enumerate(Events)]

ax.bar(x_pos, Attendees, width=0.3, label="Attendees", color="green")
ax.bar([p + 0.3 for p in x_pos], Tickets_Sold, width=0.3, label="Tickets Sold", color="blue")

ax.set_xticks([p + 0.15 for p in x_pos])
ax.set_xticklabels(Events)

for x, y1, y2 in zip(x_pos, Attendees, Tickets_Sold):
    ax.text(x-0.1, y1/2, y1, ha='center', va='bottom')
    ax.text(x+0.2, y2/2, y2, ha='center', va='bottom')

ax.legend(loc="best")
plt.tight_layout()
plt.savefig("Bar Chart/png/240.png")
plt.clf()

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,8)) 
ax = fig.add_subplot(111)

data = [[2020, 200, 100, 50, 500],
        [2021, 250, 150, 80, 400],
        [2022, 300, 200, 100, 350],
        [2023, 350, 250, 120, 300]]

x_val = [i[0] for i in data]
y1_val = [i[1] for i in data]
y2_val = [i[2] for i in data]
y3_val = [i[3] for i in data]
y4_val = [i[4] for i in data]

ax.plot(x_val, y1_val, label="Museum Visits (millions)", marker="o", c='#FFA500')
ax.plot(x_val, y2_val, label="Art Shows (millions)", marker="o", c='#1E90FF')
ax.plot(x_val, y3_val, label="Music Festivals (millions)", marker="o", c='#228B22')
ax.plot(x_val, y4_val, label="Theatre Shows (millions)", marker="o", c='#FF4500')

plt.title("Annual Art and Culture Events Participation in the US from 2020 to 2023")
plt.xlabel("Year")
plt.ylabel("Participants (millions)")
plt.legend()

ax.grid(linestyle="dotted")

for a,b in zip(x_val, y1_val):
    ax.annotate('{}'.format(b), xy=(a, b), xytext=(0,5), textcoords="offset points", ha='center', va='bottom')
for a,b in zip(x_val, y2_val):
    ax.annotate('{}'.format(b), xy=(a, b), xytext=(0,5), textcoords="offset points", ha='center', va='bottom')
for a,b in zip(x_val, y3_val):
    ax.annotate('{}'.format(b), xy=(a, b), xytext=(0,5), textcoords="offset points", ha='center', va='bottom')
for a,b in zip(x_val, y4_val):
    ax.annotate('{}'.format(b), xy=(a, b), xytext=(0,5), textcoords="offset points", ha='center', va='bottom')

plt.xticks(x_val)
plt.tight_layout()
plt.savefig("line chart/png/228.png")
plt.clf()
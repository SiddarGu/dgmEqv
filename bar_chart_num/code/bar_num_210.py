
import matplotlib.pyplot as plt
import numpy as np

country = ['USA','UK','Germany','France']
sports_teams = [60,70,50,80]
concerts = [50,60,70,60]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot()

width = 0.35
x = np.arange(len(country))

ax.bar(x, sports_teams, width, label="Sports Teams")
ax.bar(x + width, concerts, width, label="Concerts")

ax.set_ylabel("Number")
ax.set_title("Number of Sports Teams and Concerts in Four Countries in 2021")
ax.set_xticks(x + width/2)
ax.set_xticklabels(country)

ax.legend(loc="upper left")

for i, v in enumerate(sports_teams):
    ax.text(i - 0.15, v+3, str(v))

for i, v in enumerate(concerts):
    ax.text(i + 0.15, v+3, str(v))

plt.tight_layout()
plt.savefig("Bar Chart/png/176.png")
plt.clf()
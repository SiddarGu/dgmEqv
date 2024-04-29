
import matplotlib.pyplot as plt
import numpy as np

data = [[2019, 50, 100],
        [2020, 60, 130],
        [2021, 70, 150]]

fig = plt.figure()
ax = fig.add_subplot()

year = [x[0] for x in data]
deaths = [x[1] for x in data]
injuries = [x[2] for x in data]

ax.bar(year, deaths, label="Deaths", bottom=injuries)
ax.bar(year, injuries, label="Injuries")

ax.set_title("Number of deaths and injuries from 2019 to 2021")
ax.set_xticks(year)
ax.legend(loc="upper left")

for i, v in enumerate(deaths):
    ax.text(year[i]-0.2, v/2+injuries[i], str(v))
for i, v in enumerate(injuries):
    ax.text(year[i]-0.2, v/2, str(v))

fig.tight_layout()
fig.savefig("Bar Chart/png/442.png")
plt.close(fig)
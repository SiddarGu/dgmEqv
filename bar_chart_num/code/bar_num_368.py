
import matplotlib.pyplot as plt
import numpy as np

# set data
State = ["California","Texas","New York","Florida"]
Charities = [100, 80, 90, 110]
Donations = [150, 130, 140, 160]

# create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

# plot the data
ax.bar(State, Charities, color="blue", label="Charities")
ax.bar(State, Donations, color="red", bottom=Charities, label="Donations")

# add label to each bar
for x, y in zip(State, Charities):
    ax.annotate("{0:.0f}".format(y), xy=(x,y+1), ha="center", va="bottom")

for x, y in zip(State, Donations):
    ax.annotate("{0:.0f}".format(y), xy=(x,y+1), ha="center", va="bottom")

# set x label
ax.set_xticks(State)
ax.set_xticklabels(State, rotation=45, ha="right")

# set title
ax.set_title("Number of charities and donations in four states in 2021")

# add legend
ax.legend(loc="upper right")

# adjust figure
fig.tight_layout()

# save figure
fig.savefig('Bar Chart/png/358.png')

# clear figure
plt.clf()
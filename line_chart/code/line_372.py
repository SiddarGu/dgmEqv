
import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(10, 8))
ax = plt.subplot()

# set data
time = ["08:00","09:00","10:00","11:00","12:00","13:00","14:00"]
solar = [3.2,4.1,5.2,6.1,6.7,6.2,5.2]
wind = [2.4,3.1,4.2,5.2,6.1,5.4,4.1]
hydro = [1.8,2.3,2.9,3.6,4.2,3.8,3.2]

# draw line chart
plt.plot(time, solar, label="Solar Power Generation(GW)", color='red')
plt.plot(time, wind, label="Wind Power Generation(GW)", color='green')
plt.plot(time, hydro, label="Hydropower Generation(GW)", color='blue')

# set title, legend and x-axis label
plt.title("Energy production in three sources at a renewable energy plant")
plt.legend(loc="upper left")
plt.xticks(time)

# set background grids
plt.grid(True, linestyle='--', color='#a0a0a0', linewidth=1)

# automatically resize the image
plt.tight_layout()

# save image
plt.savefig("line chart/png/136.png")

# clear the current image state
plt.cla()
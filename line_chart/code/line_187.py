
import matplotlib.pyplot as plt
import numpy as np

# setting figure size
plt.figure(figsize=(10, 5))

# set data
data = np.array([[ 2021,15,60 ], 
                 [ 2022,17,65 ],
                 [ 2023,20,70 ], 
                 [ 2024,22,75 ],
                 [ 2025,25,80 ], 
                 [ 2026,27,85 ],
                 [ 2027,30,95 ]])

# set the subplot
ax = plt.subplot()

# plot data
year = data[:, 0]

temp = data[:, 1]
ax.plot(year, temp, color="r", linewidth=2, label="Temperature")

humidity = data[:, 2]
ax.plot(year, humidity, color="b", linewidth=2, label="Humidity")

# set X,Y label
ax.set_xlabel("Year")
ax.set_ylabel("Value")

# set figure title
ax.set_title("Changes in temperature and humidity from 2021 to 2027")

# set x-ticks
ax.set_xticks(year)

# set legend position
ax.legend(loc="best")

# save as absolute path
plt.savefig("line chart/png/346.png")

# clear image state
plt.clf()
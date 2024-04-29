
import matplotlib.pyplot as plt
import matplotlib

#set parameters
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

#create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#set data
year = [2019, 2020, 2021, 2022, 2023]
air_pollution = [20, 15, 25, 19, 22]
water_pollution = [7, 6, 5, 7, 6]
noise_pollution = [80, 75, 60, 65, 70]

#plot line
ax.plot(year, air_pollution, label="Air Pollution(PM2.5, micrograms/m3)", color="red", marker='o', linestyle='--')
ax.plot(year, water_pollution, label="Water Pollution(pH)", color="blue", marker='o', linestyle='--')
ax.plot(year, noise_pollution, label="Noise Pollution(dB)", color="green", marker='o', linestyle='--')

#set x, y-axis
ax.set_xticks(year)
ax.set_xticklabels(year)
ax.set_xlabel("Year", fontsize=15)
ax.set_ylabel("Value", fontsize=15)

#set legend
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

#set title
ax.set_title("Pollution in a coastal city from 2019 to 2023", fontsize=18, pad=20)

#set annotation
ax.annotate("20", xy=(2019, 20), xytext=(2020, 20), fontsize=15, arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate("15", xy=(2020, 15), xytext=(2021, 15), fontsize=15, arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate("25", xy=(2021, 25), xytext=(2022, 25), fontsize=15, arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate("19", xy=(2022, 19), xytext=(2023, 19), fontsize=15, arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate("22", xy=(2023, 22), xytext=(2022, 22), fontsize=15, arrowprops=dict(facecolor='black', shrink=0.05))

#resize image
fig.tight_layout()

#save image
plt.savefig("line chart/png/162.png")

#clear image
plt.clf()
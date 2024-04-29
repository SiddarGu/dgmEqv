
import matplotlib.pyplot as plt
import numpy as np

data = [[0,4,80,95],
        [5,9,78,90],
        [10,14,76,85],
        [15,19,74,80],
        [20,24,72,75],
        [25,29,70,70],
        [30,34,68,65],
        [35,39,66,60],
        [40,44,64,55],
        [45,49,62,50],
        [50,54,60,45],
        [55,59,58,40],
        [60,64,56,35],
        [65,69,54,30],
        [70,74,52,25],
        [75,79,50,20],
        [80,84,48,15],
        [85,89,46,10],
        [90,94,44,5],
        [95,99,42,0]]

x_labels = [f"{data[i][0]}-{data[i][1]}" for i in range(len(data))]
y_life = [data[i][2] for i in range(len(data))]
y_vacc = [data[i][3] for i in range(len(data))]

fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot(111)
ax.set_title("Average life expectancy and vaccination rate of different age groups in the United States in 2021")

ax.plot(x_labels, y_life, color="blue", label="Average life expectancy(years)")
ax.plot(x_labels, y_vacc, color="red", label="Vaccination rate")
ax.grid(True, linestyle="-.", color="gray")
ax.set_xticks(x_labels)

for i in range(len(data)):
    ax.annotate(f"{y_life[i]}", xy=(x_labels[i], y_life[i]), rotation=45, fontsize=10)
    ax.annotate(f"{y_vacc[i]}", xy=(x_labels[i], y_vacc[i]), rotation=45, fontsize=10)

ax.legend(bbox_to_anchor=(1, 1), loc="upper left")
plt.tight_layout()
plt.savefig("./line chart/png/540.png")
plt.clf()
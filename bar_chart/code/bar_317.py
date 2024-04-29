
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

Year = np.array(["2020","2021","2022","2023"])
Patents_Filed = np.array([1200,1000,1300,900])
Research_Projects_Completed = np.array([250,350,500,400])

ax.bar(Year,Patents_Filed, label = 'Patents Filed', bottom=Research_Projects_Completed)
ax.bar(Year,Research_Projects_Completed, label = 'Research Projects Completed')

ax.set_title("Patents filed and research projects completed in science and engineering from 2020 to 2023")
ax.set_xlabel("Year")
ax.set_ylabel("Number")
ax.legend(loc="upper left")
ax.grid(axis="y", alpha=0.3)
plt.xticks(Year)
plt.tight_layout()
plt.savefig("bar chart/png/388.png")
plt.clf()
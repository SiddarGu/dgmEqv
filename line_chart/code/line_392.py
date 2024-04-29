

import matplotlib.pyplot as plt

age = ["0-5", "6-12", "13-18", "19-25", "26-35", "36-45", "46-60", "61-100"]
weight = [15, 25, 45, 55, 65, 75, 85, 65]
height = [1.2, 1.5, 1.8, 1.9, 1.7, 1.6, 1.5, 1.4]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1,1,1)
ax.plot(age, weight, 'g', label="Average Weight (kg)")
ax.plot(age, height, 'b', label="Average Height (m)")
ax.set_xlabel("Age")
ax.set_xticks(age)
ax.set_ylabel("Value")
ax.set_title("Average Weight and Height of People in Different Age Groups")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig("line chart/png/128.png", bbox_inches = 'tight')
plt.clf()
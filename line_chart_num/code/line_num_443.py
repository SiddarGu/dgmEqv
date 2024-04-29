
import matplotlib.pyplot as plt
import numpy as np

age = [18, 19, 20, 21, 22, 23]
bmi = [20.5, 21.7, 23.2, 25.5, 27.3, 29.1]
bp = [120/80, 125/85, 130/90, 135/95, 140/100, 145/105]
bgl = [5.3, 6.5, 7.2, 7.8, 8.4, 9.2]

fig = plt.figure(figsize = (12, 8))
ax = plt.subplot()

plt.plot(age, bmi, label = "BMI", linewidth = 3)
plt.plot(age, bp, label = "BP", linewidth = 3)
plt.plot(age, bgl, label = "BGL", linewidth = 3)

for a, b, c, d in zip(age, bmi, bp, bgl):
    plt.annotate(str(b) + "/" + str(c) + "/" + str(d), xy = (a, b))

ax.set_title("Changes in health indicators among people aged 18-23")
ax.set_xlabel("Age")
ax.set_ylabel("Values")

ax.set_xticks(age)
ax.grid()

ax.legend()

plt.tight_layout()
plt.savefig("line chart/png/310.png")
plt.clf()
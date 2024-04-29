
import matplotlib.pyplot as plt
import numpy as np

age = ["0-17", "18-35", "36-50", "51-65", "66-80", "81-100"]
male_mortality = [5, 3, 7, 12, 25, 45]
female_mortality = [4, 2, 5, 9, 20, 40]

fig = plt.figure(figsize = (10, 6))
ax = fig.add_subplot()
ax.plot(age, male_mortality, label="Male Mortality Rate(%)", marker="o", color="blue")
ax.plot(age, female_mortality, label="Female Mortality Rate(%)", marker="o", color="red")
ax.grid(True)
ax.set_xticklabels(age, rotation=45, ha="right")
ax.legend(loc="upper center")
ax.set_title("Mortality Rates of Males and Females in Different Age Groups in 2020")
plt.tight_layout()
plt.savefig("line chart/png/211.png")
plt.clf()
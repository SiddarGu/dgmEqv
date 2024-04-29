
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[18,45,20,5000],
                 [25,50,18,6000],
                 [35,55,15,7000],
                 [45,65,10,8000],
                 [55,75,4,9000]])

age, employment_rate, unemployment_rate, salary = data.T

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1, 1, 1)

ax.plot(age, employment_rate, label="Employment Rate", marker='o', color="g")
ax.plot(age, unemployment_rate, label="Unemployment Rate", marker='o', color="b")

ax.set_xlabel("Age")
ax.set_ylabel("Percentage(%)")

ax.set_title("Employment and Unemployment Rates of Different Age Groups in the US in 2021")

ax.legend(loc="best")

for i, txt in enumerate(salary):
    ax.annotate(txt, (age[i],employment_rate[i]), rotation=45, ha='right', wrap=True)

plt.xticks(age)

plt.tight_layout()

plt.savefig("line chart/png/387.png")

plt.clf()
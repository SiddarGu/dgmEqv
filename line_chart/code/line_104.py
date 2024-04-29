
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))

ax = fig.add_subplot(111)

Age = ["18-24", "25-34", "35-44", "45-54", "55-64", "65 and over"]
Employment_Rate = [42, 54, 58, 50, 48, 30]

plt.plot(Age, Employment_Rate, color='midnightblue', linewidth=2)
plt.xticks(np.arange(len(Age)), Age, rotation=45, ha="right", rotation_mode="anchor")

ax.set_title("Employment rate of different age groups in the US in 2021")
ax.set_ylabel("Employment Rate(%)")

plt.tight_layout()
plt.savefig('line chart/png/333.png')
plt.clf()
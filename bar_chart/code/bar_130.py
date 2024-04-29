
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot()
country = ["USA", "UK", "Germany", "France"]
education_index = [80, 72, 76, 70]
health_index = [90, 85, 88, 86]
ax.bar(country, education_index, label="Education Index", color='g')
ax.bar(country, health_index, label="Health Index", bottom=education_index, color='b')
ax.set_title("Social Science and Humanities Index of four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Index")
ax.set_ylim(0, 110)
ax.legend(loc="upper right")
ax.grid(True)
plt.xticks(rotation=30)

fig.tight_layout()
plt.savefig('bar chart/png/385.png')
plt.clf()
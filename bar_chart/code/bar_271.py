
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
ax = plt.subplot()

data = np.array([[200, 5000], [500, 1500], [1000, 1000]])
categories = ["Air", "Rail", "Road"]
bar_width = 0.4

passengers = data[:, 0]
distance = data[:, 1]

ax.bar(np.arange(len(categories)), passengers, width=bar_width, label="Passengers(thousand)")
ax.bar(np.arange(len(categories)) + bar_width, distance, width=bar_width, label="Distance(km)")

ax.set_xticks(np.arange(len(categories)))
ax.set_xticklabels(categories, rotation=0, wrap=True)
ax.set_title("Number of passengers and distance traveled by different modes of transportation in 2021")
ax.legend(loc="best")

plt.tight_layout()
plt.savefig('bar chart/png/197.png')
plt.clf()
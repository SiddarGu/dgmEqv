
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[3,17], [2.5,19], [1.2,10], [2.7, 15]])

plt.figure(figsize=(10,6))
ax = plt.subplot()

plt.bar(data[:,0], data[:,1], width=0.5, color='#33D1FF')

ax.set_xticks(data[:,0])
ax.set_xticklabels(["Facebook", "Instagram", "Twitter", "YouTube"], rotation=30, wrap=True)
ax.set_title("User and Engagement Statistics for Popular Social Media Platforms in 2021")
plt.tight_layout()
plt.savefig("bar chart/png/332.png")
plt.clf()
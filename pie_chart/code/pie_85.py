
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)

labels = ["Visual Arts", "Music", "Dance", "Theatre", "Cinema", "Literature", "Other"]
sizes = [25, 18, 10, 15, 15, 10, 7]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6','#c2c2f0','#ff8080']

ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',startangle=90)
ax.axis('equal')
plt.title("Distribution of Arts and Culture in the US, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/71.png')
plt.xticks(np.arange(0, 360, 90))
plt.show()
plt.clf()
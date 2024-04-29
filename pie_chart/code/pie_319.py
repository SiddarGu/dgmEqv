
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 8))
ax = plt.subplot()

labels = ['Male', 'Female']
sizes = [45, 55]

ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title("Gender Distribution in the USA, 2023")
plt.tight_layout()
plt.xticks(rotation=90, ha='center')

fig = plt.gcf()
fig.set_size_inches(8, 8)
plt.savefig("pie chart/png/438.png")
plt.clf()
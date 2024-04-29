
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

Modes = np.array(['Air','Rail','Road','Maritime'])
Percentage = np.array([25,20,35,20])

ax.pie(Percentage, labels=Modes, startangle=90, autopct='%.1f%%', textprops={'fontsize': 14})
ax.set_title("Mode of Transportation Distribution in the Global Logistics Industry, 2023")
ax.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/73.png')
plt.clf()
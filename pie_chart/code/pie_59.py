

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6, 6))
types = ['Leisure','Business','Education','Religious','Medical','Adventure']
percentage = [40, 20, 15, 10, 10, 5]

plt.pie(percentage, labels=types, autopct='%1.1f%%', textprops={'fontsize': 8},
        wedgeprops = {'linewidth': 1, 'edgecolor': 'black'}, startangle=90)
plt.title("Types of Tourism in the World, 2023", fontsize=14)
plt.axis('equal')
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.tight_layout()
plt.xticks([])
plt.savefig("pie chart/png/142.png")
plt.clf()
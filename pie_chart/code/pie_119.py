
import matplotlib.pyplot as plt 
import numpy as np

labels = ["Domestic", "Foreign", "Business", "Others"]
sizes = [50, 30, 10, 10]

fig, ax = plt.subplots(figsize=(4, 4))
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.68)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ax.set_title('Tourist Distribution in the USA in 2023', fontsize=12, pad=12)
ax.text(-0.2, 0.1, 'Travelers', fontsize=10)

plt.tight_layout()
plt.savefig('pie chart/png/322.png')
plt.clf()
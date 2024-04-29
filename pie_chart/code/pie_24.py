
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
labels = ['18-25', '26-35', '36-45', '46-55', '55+']
sizes = [20, 30, 20, 15, 15]

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, labeldistance=1.1)
ax.axis('equal')
ax.set_title("Healthcare Utilization by Age Group in the USA, 2023", fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/44.png', bbox_inches='tight')

plt.clf()
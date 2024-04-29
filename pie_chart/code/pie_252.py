
import matplotlib.pyplot as plt
import numpy as np

labels = ['Professional Employees', 'Administrative Employees', 'Technical Employees', 'Sales Employees', 'Other Employees']
sizes = [35, 25, 15, 15, 10]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12}, wedgeprops={'linewidth': 1, 'edgecolor': 'black'})
ax.set_title('Employee Distribution in a Corporate Workforce, 2023', fontsize=14)
plt.tight_layout()
plt.savefig('pie chart/png/58.png')
plt.clf()
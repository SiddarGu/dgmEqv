
import matplotlib.pyplot as plt
import numpy as np

# The data to plot
labels = 'Income Tax', 'Social Security Tax', 'Corporate Tax', 'Property Tax', 'Sales Tax', 'Excise Tax', 'Other'
sizes = [41, 19, 15, 10, 7, 3, 5]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'lavender', 'pink']

# Draw the figure
plt.figure(figsize=(12, 9))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Breakdown of Tax Revenue Sources in the United States,2023')
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/149.png')
plt.clf()
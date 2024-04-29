
import matplotlib.pyplot as plt
import numpy as np

labels = ['Air', 'Rail', 'Water', 'Road', 'Other']
percentage = [25, 20, 20, 30, 5]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.axis('equal')

ax.pie(percentage, labels=labels, autopct='%1.1f%%', 
       startangle=90, shadow=True, wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'dashed'})

plt.title("Distribution of Transportation Modes in the USA, 2023", fontsize=12)
plt.tight_layout()
plt.savefig('pie chart/png/152.png')
plt.clf()
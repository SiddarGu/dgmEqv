
import matplotlib.pyplot as plt
import numpy as np

labels = ['Visual Arts', 'Music', 'Theatre', 'Dance', 'Literature']
percentage = [30, 20, 20, 15, 15]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(percentage, labels=labels, autopct='%1.1f%%', textprops={'fontsize':14})
ax.set_title('Distribution of Artforms in the Arts and Culture World, 2023')
plt.axis('equal') 
plt.tight_layout()
plt.xticks(rotation=45, wrap=True)
plt.savefig('pie chart/png/205.png')
plt.clf()
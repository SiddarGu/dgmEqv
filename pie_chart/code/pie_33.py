
import matplotlib.pyplot as plt
import numpy as np

labels = 'Windows', 'MacOS', 'Linux', 'Android', 'iOS'
sizes = [48, 19, 8, 21, 4]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  
ax.set_title("Operating System Usage in the World, 2023")
ax.legend(loc='upper left',bbox_to_anchor=(0.8,0.95))
plt.xticks(rotation=45) 
plt.tight_layout()
plt.savefig("pie chart/png/156.png")
plt.clf()
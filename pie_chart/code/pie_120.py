

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['Laptop','Tablet','Mobile Phone','Desktop Computer','Wearable Tech']
sizes = [30,20,35,10,5]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal')
ax.set_title('Breakdown of Popular Device Types in the Digital Age, 2023', fontsize=14)
plt.tight_layout()
plt.savefig('pie chart/png/491.png')
plt.show()
plt.close()
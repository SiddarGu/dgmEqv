
import matplotlib.pyplot as plt
import numpy as np

labels = ['18-24','25-35','36-45','46-65','65+']
sizes = np.array([20,30,20,20,10])

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.f%%', startangle=90,textprops={'fontsize': 14})
ax.axis('equal')
ax.set_title('Voter Demographics in the US in 2023', fontsize=16)
plt.tight_layout()
plt.savefig('pie chart/png/41.png')
plt.clf()
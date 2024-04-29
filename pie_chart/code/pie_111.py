
import matplotlib.pyplot as plt
import numpy as np

labels = np.array(['Facebook','YouTube','Twitter','Instagram','WhatsApp','LinkedIn','Snapchat','Other'])
sizes = np.array([35,20,10,15,10,5,5,10])

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'rotation':90, 'wrap':True})
ax.set_title("Social Media Platform Usage in the USA, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/169.png')
plt.clf()
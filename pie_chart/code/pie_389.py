
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6))
labels = ['Automotive','Aerospace','Electronics','Metal and Machinery','Chemical','Other']
sizes = [30,20,15,15,10,10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90, textprops={'fontsize': 12, 'wrap': True, 'rotation': 20})

plt.title('Distribution of Manufacturing Industries in the Global Market, 2023', fontsize=16)

plt.xticks(np.arange(0.0, 360.0, 90.0))
plt.tight_layout()
plt.savefig('pie chart/png/459.png')
plt.clf()
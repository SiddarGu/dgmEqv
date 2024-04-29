
import matplotlib.pyplot as plt
import numpy as np 

labels=['Cash Donations', 'Volunteering', 'In-Kind Donations', 'Online Donations', 'Others']
percentage = [50, 25, 10, 10, 5]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)

ax.pie(percentage,labels=labels,autopct='%1.1f%%',startangle=90)
ax.axis('equal')

plt.title('Contributions to Charities and Nonprofits in the USA, 2023')

plt.savefig('pie chart/png/353.png')
plt.tight_layout()
plt.xticks([])
plt.show()
plt.clf()
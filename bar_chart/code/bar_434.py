
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[500, 10], [1000, 20], [800, 15], [400, 7]])
Organization = ['Red Cross', 'World Vision', 'UNICEF', 'Greenpeace']

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
width = 0.3

ax.bar(np.arange(len(data))-width, data[:,0], width, label='Donors')
ax.bar(np.arange(len(data)), data[:,1], width, label='Donations(million)')

ax.set_xticks(np.arange(len(data)))
ax.set_xticklabels(Organization, rotation=45, ha='right', wrap=True)
ax.set_title('Donors and donations of four charity organizations in 2021')
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/98.png')
plt.clf()
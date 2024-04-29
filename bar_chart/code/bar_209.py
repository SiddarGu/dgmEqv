
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

states = ['New York','California','Texas','Florida']
orgs = [100, 120, 110, 90]
dons = [300, 400, 350, 380]

width = 0.35
x_pos = np.arange(len(states))

ax.bar(x_pos, orgs, width, label='Number of Organizations', color='#0072BC')
ax.bar(x_pos+width, dons, width, label='Annual Donations (million)', color='#ED1C24')

ax.set_title('Number of Charity and Nonprofit Organizations and Annual Donations in Four States 2021')
ax.set_xticks(x_pos+width/2)
ax.set_xticklabels(states, rotation=90, wrap=True)
ax.legend()
ax.grid(which='major', axis='y', linestyle='--')

plt.tight_layout()
plt.savefig('bar chart/png/176.png')
plt.clf()
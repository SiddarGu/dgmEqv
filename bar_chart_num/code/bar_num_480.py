
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot()

#data
country = ['USA', 'UK', 'Germany', 'France']
humans_rights_index = [80, 90, 85, 75]
freedom_index = [50, 60, 55, 45]
off_grid_energy_access = [20, 30, 25, 15]

#figure
x = np.arange(len(country)) 
width = 0.25

ax.bar(x-width, humans_rights_index, width=width, label='Human Rights Index', color='orange')
ax.bar(x, freedom_index, width=width, label='Freedom Index', color='green')
ax.bar(x+width, off_grid_energy_access, width=width, label='Off-grid Energy Access Index', color='blue')

#x-axes
ax.set_xticks(x)
ax.set_xticklabels(country)

#legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), shadow=True, ncol=4)

#title
ax.set_title('Social and Human Development Indices of four countries in 2021')

#labels
for i, v in enumerate(humans_rights_index):
    ax.text(i-width+0.07, v+0.5, str(v), color='black', fontweight='bold')

for i, v in enumerate(freedom_index):
    ax.text(i+0.07, v+0.5, str(v), color='black', fontweight='bold')

for i, v in enumerate(off_grid_energy_access):
    ax.text(i+width+0.07, v+0.5, str(v), color='black', fontweight='bold')

#adjusting
plt.tight_layout()

#save
plt.savefig('Bar Chart/png/239.png')

#clear
plt.clf()

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 8))

orgs = ['Red Cross', 'World Vision', 'UNICEF', 'Save the Children']
donations = [200, 180, 230, 150]
volunteers = [500, 400, 470, 350]

x = np.arange(len(orgs))
ax.bar(x - 0.2, donations, width=0.4, label='Donations (million)', color='#1f77b4')
ax.bar(x + 0.2, volunteers, width=0.4, label='Volunteers', color='#ff7f0e')

ax.set_xticks(x)
ax.set_xticklabels(orgs, fontsize=14, rotation=45, ha='right', va='top', wrap=True)
ax.set_title('Charitable donations and volunteers in four nonprofit organizations in 2021', fontsize=18)
ax.legend(fontsize=14)

plt.tight_layout()
plt.savefig('bar chart/png/351.png')
plt.clf()
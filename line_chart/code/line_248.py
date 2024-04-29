
import matplotlib.pyplot as plt
import numpy as np

month = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
prod = np.array([500, 550, 650, 700, 600, 650, 700, 750, 650, 700, 650, 700])
eff = np.array([70, 75, 80, 85, 90, 95, 80, 85, 90, 95, 80, 75])

fig, ax = plt.subplots(figsize=(10, 6)) 

ax.plot(month, prod, label='Productivity (units per hour)')
ax.plot(month, eff, label='Efficiency (%)')

ax.set_title('Monthly Productivity and Efficiency of a Manufacturing Plant in 2020', fontsize=18)
ax.set_xlabel('Month', fontsize=14)

ax.legend(loc='best', fontsize=14, framealpha=.9)
ax.tick_params(axis='both', which='major', labelsize=14)

fig.tight_layout()
plt.xticks(month)

plt.savefig('line chart/png/526.png', dpi=300)
plt.clf()
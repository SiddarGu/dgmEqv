
import matplotlib.pyplot as plt
import numpy as np

Month = np.array(['January', 'February', 'March', 'April'])
Museums = np.array([20000, 22000, 25000, 30000])
Galleries = np.array([30000, 35000, 40000, 45000])
Theaters = np.array([25000, 28000, 30000, 35000])

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(Month, Museums, label='Museums')
ax.plot(Month, Galleries, label='Galleries')
ax.plot(Month, Theaters, label='Theaters')
ax.set_title('Monthly Visitors to Arts and Culture Institutions in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Visitors')
ax.set_xticks(Month)
ax.legend(loc='lower right')
plt.tight_layout()
plt.savefig('line chart/png/170.png')
plt.clf()
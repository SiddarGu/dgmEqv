
import matplotlib.pyplot as plt
import numpy as np

donor = ['Individual','Corporate','Government','Other Organizations']
amount_donated = [1000,5000,10000,3000]

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
ax.plot(donor,amount_donated,c='black',linewidth=3)
ax.set_title('Donations to Charity Organizations in 2021', fontsize=20)
ax.set_xlabel('Donor', fontsize=15)
ax.set_ylabel('Amount Donated', fontsize=15)
ax.set_xticklabels(donor, rotation=45, fontsize=12, wrap=True)
ax.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/29.png')
plt.clf()
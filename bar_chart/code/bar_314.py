
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

orgs = ['Charity A','Charity B','Charity C','Charity D']
donors = [3000,5000,4000,6000]
funds = [20,30,25,35]

ax.bar(orgs, donors, label='Donors', width=0.4, bottom=0)
ax.bar(orgs, funds, label='Funds Raised (million)', width=0.4, bottom=np.array(donors))

ax.set_title('Donors and funds raised by four charity organizations in 2021')

ax.set_xticklabels(orgs, rotation=45, ha="right", wrap=True)
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/56.png')
plt.clf()
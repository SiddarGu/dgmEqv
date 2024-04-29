
import matplotlib.pyplot as plt
import numpy as np

# set data
country = ['USA','UK','Germany','France']
tax_rate = [25,30,28,35]
public_spending = [500,550,600,650]

# create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# plotting
ax.bar(country, tax_rate, width=0.4, label='Tax Rate(%)', color='#539caf',align='center')
ax.bar(country, public_spending, width=0.4, label='Public Spending(billion)', color='#7663b0',align='center', bottom=tax_rate)

# label
ax.set_xlabel('Country')
ax.set_ylabel('Tax Rate & Public Spending')
ax.set_title('Tax rate and public spending in four countries in 2021')
ax.set_xticks(country)
ax.legend(loc='upper left')

# add grid
ax.grid(axis='y', linestyle='--')

# figure layout
fig.tight_layout()

# save
fig.savefig('bar_107.png')

# clear current image state
plt.cla()
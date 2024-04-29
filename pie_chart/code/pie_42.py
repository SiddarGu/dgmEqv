
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

tax_revenues = [35, 15, 25, 15, 10]
tax_types = ['Income Tax', 'Corporate Tax', 'Sales Tax', 'Property Tax', 'Other']

ax.pie(tax_revenues, labels=tax_types, autopct='%1.1f%%', textprops={'fontsize': 14}, wedgeprops={'linewidth': 2, 'edgecolor':'white'})

ax.legend(loc="center right", bbox_to_anchor=(1.2, 0.5), fontsize=14)
ax.set_title('Distribution of Tax Revenues in the USA, 2023', fontsize=14)

plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/416.png', bbox_inches='tight')
plt.clf()
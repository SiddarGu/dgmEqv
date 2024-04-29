
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

data = {'Country':['USA','UK','Germany','France'],
        'Voter Turnout(%)':[60,70,75,80],
        'Tax Rate(%)':[20,25,30,35],
        'Unemployment Rate(%)':[3.5,4.2,5.3,6.7]}

x = data['Country']
voter_turnout = data['Voter Turnout(%)']
tax_rate = data['Tax Rate(%)']
unemployment_rate = data['Unemployment Rate(%)']

ax.bar(x, voter_turnout, width=0.2, label='Voter Turnout(%)', color='#e6194b')
ax.bar(x, tax_rate, width=0.2, bottom=voter_turnout, label='Tax Rate(%)', color='#3cb44b')
ax.bar(x, unemployment_rate, width=0.2, bottom=[i+j for i,j in zip(voter_turnout, tax_rate)], label='Unemployment Rate(%)', color='#ffe119')

ax.legend(loc='upper left')
ax.set_title('Government and Public Policy Indicators of Four Countries in 2021', fontsize=14, fontweight='bold')
ax.set_xticklabels(x, rotation=45, fontsize=10)
fig.tight_layout()
plt.savefig('bar chart/png/299.png')
plt.clf()
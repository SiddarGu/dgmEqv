
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Votes = [20000, 30000, 18000, 23000]
Voters = [45000, 50000, 40000, 47000]
Turnout = [44.44, 60.00, 45.00, 48.94]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.bar(Country, Turnout, bottom=0, color='green')
ax.set_ylabel('Voting Turnout (%)')
ax.set_title('Voting turnout in four countries in 2021')
ax.set_xticklabels(Country, rotation=45, ha='right', wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/245.png')
plt.clf()
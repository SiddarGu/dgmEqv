
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

years = [2001, 2002, 2003, 2004]
cases_filed = [500, 550, 600, 650]
cases_settled = [400, 450, 500, 550]
cases_dismissed = [100, 130, 150, 180]
cases_won = [200, 220, 250, 280]

ax.plot(years, cases_filed, label='Cases Filed')
ax.plot(years, cases_settled, label='Cases Settled')
ax.plot(years, cases_dismissed, label='Cases Dismissed')
ax.plot(years, cases_won, label='Cases Won')

plt.xticks(np.arange(min(years), max(years)+1, 1))
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=4, fontsize='medium')
plt.title("Case Outcomes in the US Legal System in the 21st Century")
plt.tight_layout()
plt.savefig('line chart/png/485.png')
plt.clf()
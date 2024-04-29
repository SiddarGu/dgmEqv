
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Legislation = [2500, 3000, 2200, 2500]
Courts = [1500, 1800, 1400, 1700]

fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot()
ax.set_title("Number of legislation and courts in four countries in 2021")
ax.bar(Country, Legislation, label='Legislation', bottom=Courts)
ax.bar(Country, Courts, label='Courts')
ax.set_xticks(np.arange(len(Country)))
ax.set_xticklabels(Country, rotation=45, ha="right", wrap=True)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('bar chart/png/453.png')
plt.clf()
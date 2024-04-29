
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig, ax = plt.subplots()
fig.set_size_inches(10, 6)
ax.bar('USA', [2,3,5], label='food A', bottom=0, width=0.2, align='center')
ax.bar('USA', [0,0,0], label='food B', bottom=2, width=0.2, align='center')
ax.bar('USA', [0,0,0], label='food C', bottom=5, width=0.2, align='center')
ax.bar('UK', [2.5,3.5,4.5], label='food A', bottom=0, width=0.2, align='center')
ax.bar('UK', [0,0,0], label='food B', bottom=2.5, width=0.2, align='center')
ax.bar('UK', [0,0,0], label='food C', bottom=4.5, width=0.2, align='center')
ax.bar('Germany', [3,4,5.5], label='food A', bottom=0, width=0.2, align='center')
ax.bar('Germany', [0,0,0], label='food B', bottom=3, width=0.2, align='center')
ax.bar('Germany', [0,0,0], label='food C', bottom=5.5, width=0.2, align='center')
ax.bar('France', [2.7,4.2,5.2], label='food A', bottom=0, width=0.2, align='center')
ax.bar('France', [0,0,0], label='food B', bottom=2.7, width=0.2, align='center')
ax.bar('France', [0,0,0], label='food C', bottom=5.2, width=0.2, align='center')
ax.set_title('Prices of food A, B and C in four countries in 2021')
ax.set_xticks(['USA','UK','Germany','France'])
ax.set_xticklabels(['USA','UK','Germany','France'], rotation=90, wrap=True)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.grid(axis='y')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/382.png')
plt.clf()
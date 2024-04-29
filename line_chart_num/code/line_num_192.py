
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
year=[2019,2020,2021,2022]
viewers=[400,500,600,750]
ad_rev=[200,250,300,400]
sp_rev=[150,180,210,240]
ax.plot(year, viewers, label='Viewers (million people)', color='#0f7d7e', marker='o', markersize=5, linestyle='-')
ax.plot(year, ad_rev, label='Advertising Revenue (million dollars)', color='#9b5f8d', marker='o', markersize=5, linestyle='-')
ax.plot(year, sp_rev, label='Sponsorship Revenue (million dollars)', color='#e6b1b1', marker='o', markersize=5, linestyle='-')
ax.set_title('Global Sports Entertainment Viewership and Revenue Changes from 2019 to 2022')
ax.set_xticks(year)
ax.grid(True, linestyle='-.')
ax.legend(loc='best')
for x, y in zip(year, viewers):
    ax.annotate('%s' %y, xy=(x, y), textcoords='data', fontsize=12, color='#0f7d7e')
for x, y in zip(year, ad_rev):
    ax.annotate('%s' %y, xy=(x, y), textcoords='data', fontsize=12, color='#9b5f8d')
for x, y in zip(year, sp_rev):
    ax.annotate('%s' %y, xy=(x, y), textcoords='data', fontsize=12, color='#e6b1b1')
plt.tight_layout()
plt.savefig('line chart/png/34.png')
plt.clf()
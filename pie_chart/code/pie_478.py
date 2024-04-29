
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# create figure
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)

# set data
data = {'Production Categories': ['Electronics', 'Automotive', 'Industrial Machinery', 'Aerospace', 'Chemical'],
        'Percentage': [0.25, 0.20, 0.30, 0.15, 0.10]}

# plot data
ax.pie(data['Percentage'], labels=data['Production Categories'], autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title('Distribution of Production in the Manufacturing Industry, 2023')
ax.axis('equal')

# set legend
ax.legend(bbox_to_anchor=(1.0, 0.5), loc="center right", fontsize=10)

# format ticks
ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_ticks_position('none')

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('pie chart/png/400.png')

# clear current image state
plt.clf()

fig = plt.figure()
ax = fig.add_subplot()

Solar = [1000, 900, 1100, 800]
Wind = [1200, 1300, 1400, 1500]
Hydro = [800, 1100, 1200, 1400]

x = np.arange(len(Solar))  # the label locations
width = 0.25  # the width of the bars

rects1 = ax.bar(x - width/2, Solar, width, label='Solar Energy(kWh)')
rects2 = ax.bar(x + width/2, Wind, width, label='Wind Energy(kWh)')
rects3 = ax.bar(x + 1.5*width, Hydro, width, label='Hydro Energy(kWh)')

ax.set_ylabel('Energy output(kWh)')
ax.set_title('Energy output of Solar, Wind and Hydro sources in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(('USA', 'UK', 'Germany', 'France'))
ax.legend(loc = 'upper right')

# Add some text for labels, title and custom x-axis tick labels, etc.
for rect in rects1:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 2),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    
for rect in rects2:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 2),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

for rect in rects3:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 2),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/614.png')

plt.clf()
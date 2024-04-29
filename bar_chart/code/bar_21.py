
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Number of sports and entertainment events in four countries in 2021')

Country = ['USA', 'UK', 'Germany', 'France']
Sports_Events = [400, 500, 300, 370]
Entertainment_Events = [500, 550, 450, 480]

ax.bar(Country, Sports_Events, label='Sports Events', bottom=Entertainment_Events, width=0.3)
ax.bar(Country, Entertainment_Events, label='Entertainment Events', width=0.3)

ax.set_xticks(Country)
ax.set_ylabel('Events')
ax.set_xlabel('Country')
ax.legend(loc='best')

plt.tight_layout()
fig.savefig('bar chart/png/542.png', bbox_inches='tight')
plt.clf()
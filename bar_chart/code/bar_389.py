
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

ax.bar(x=['Road', 'Rail', 'Air', 'Sea'], height=[50,90,400,20], width=0.4, bottom=0, label='Average Speed (km/h)', color='b')
ax.bar(x=['Road', 'Rail', 'Air', 'Sea'], height=[100,150,200,800], width=0.4, bottom=0, label='Capacity', color='r')

ax.set_title('Average speed and capacity of four different modes of transportation in 2021')
ax.set_xlabel('Mode')
ax.set_ylabel('Value')
ax.legend(loc='upper left', bbox_to_anchor=(0.1, 1))

plt.xticks(rotation=45, horizontalalignment='right', wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/231.png')
plt.clf()

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.set_title('Houses sold and Average Price in four regions in 2021')
plt.xticks(rotation=60)
ax.bar(x=['East','West','South','North'], height=[50,40,60,70], label='Houses Sold (thousands)', width=0.4, color='tab:blue')
ax.bar(x=['East','West','South','North'], height=[45,50,35,40], bottom=[50,40,60,70], label='Average Price (thousand dollar)', width=0.4, color='tab:orange')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/145.png')
plt.clf()

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot()
ax.bar(x=['USA','UK','Germany','France'], height=[450,500,400,430], label='Literature', width=0.4, bottom=0)
ax.bar(x=['USA','UK','Germany','France'], height=[550,600,480,570], label='Music', width=0.4, bottom=450)
ax.bar(x=['USA','UK','Germany','France'], height=[250,280,220,250], label='Philosophy', width=0.4, bottom=1000)
plt.xticks(rotation=90, wrap=True)
plt.title('Number of published works in social sciences and humanities in four countries in 2021')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/38.png')
plt.clf()
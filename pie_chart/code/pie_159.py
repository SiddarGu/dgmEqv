
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

labels = ['Twitter','YouTube','Instagram','Snapchat','Reddit','LinkedIn','Pinterest']
sizes = [12, 25, 20, 15, 10, 10, 8]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 13})
ax.axis('equal')

plt.title('Popularity of Social Media Platforms in the US, 2023', fontsize=15)
plt.tight_layout()
ax.xaxis.set_major_formatter(mtick.PercentFormatter())
plt.savefig('pie chart/png/472.png')
plt.close()
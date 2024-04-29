

import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
ax = plt.subplot()

month = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
hours = [6, 7, 8, 9, 10, 11, 12, 11, 10, 9, 8, 7]

plt.plot(month, hours, marker='o', linestyle='-', color='b')
plt.title('Change in Average Number of Hours on the Internet in 2021')
plt.xlabel('Month')
plt.ylabel('Average Number of Hours on the Internet')

for i, txt in enumerate(hours):
    ax.annotate(txt, (month[i],hours[i]), rotation=45, horizontalalignment='right', verticalalignment='bottom')

plt.xticks(month)
plt.tight_layout()

plt.savefig('line chart/png/356.png')
plt.clf()
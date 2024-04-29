
import matplotlib.pyplot as plt
import numpy as np

destinations = ['USA', 'UK', 'Spain', 'France', 'Italy', 'Germany', 'Japan', 'Other']
percentage = [25, 15, 20, 15, 10, 7, 5, 3]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

ax.pie(percentage, labels=destinations, autopct='%1.1f%%', textprops={'fontsize': 14})
ax.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.), fontsize=14)
ax.set_title('International Travel Destinations in 2023', fontsize=16, pad=20)

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/412.png')
plt.clf()
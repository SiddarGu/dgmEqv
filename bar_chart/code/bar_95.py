
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Social_Media_Users = [200, 250, 180, 220]
Web_Users = [400, 420, 390, 410]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.bar(Country, Social_Media_Users, width=0.3, label='Social Media Users', align='center', bottom=Web_Users)
ax.bar(Country, Web_Users, width=0.3, label='Web Users', align='center')

ax.set_title('Number of social media and web users in four countries in 2021')
ax.legend(loc='upper left')
plt.xticks(rotation=45, wrap=True)

plt.tight_layout()
plt.savefig('bar chart/png/68.png')
plt.clf()
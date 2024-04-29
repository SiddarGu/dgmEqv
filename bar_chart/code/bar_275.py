
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA","UK","Germany","France"]
Social_Media_Users = [220,130,190,150]
Web_Users = [350,240,290,210]

fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(111)
ax.bar(Country, Social_Media_Users, width=0.4, color='b', label='Social Media Users')
ax.bar(Country, Web_Users, width=0.4, bottom=Social_Media_Users, color='g', label='Web Users')
plt.xticks(np.arange(len(Country)), Country,rotation=30)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.set_title('Social media and web user count in four countries in 2021', fontsize=18)
plt.tight_layout()
plt.savefig('bar chart/png/194.png')
plt.clf()
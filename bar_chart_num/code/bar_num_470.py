
import matplotlib.pyplot as plt
x = ['January','February','March','April']
sports = [20,25,18,22]
entertainment = [30,40,45,50]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.bar(x, sports, 0.35, color='b', label='Sports Events')
ax.bar(x, entertainment, 0.35, color='y', bottom=sports, label='Entertainment Events')
plt.title('Number of sports and entertainment events from January to April 2021')
plt.xlabel('Month')
plt.ylabel('Events')
for i, v in enumerate(sports):
 ax.annotate(str(v), xy=(i, v+1), va='center')
for i, v in enumerate(entertainment):
 ax.annotate(str(v), xy=(i, sports[i]+v+1), va='center')
ax.legend(loc='upper right')
plt.xticks(x)
fig.tight_layout()
plt.savefig('Bar Chart/png/46.png', bbox_inches='tight')
plt.clf()
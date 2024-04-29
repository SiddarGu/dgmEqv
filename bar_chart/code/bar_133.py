
import matplotlib.pyplot as plt
plt.figure(figsize=( 10, 8))
ax = plt.subplot()

ax.bar([1,2,3,4], [50,40,45,35],label='Judges')
ax.bar([1,2,3,4], [200,190,180,170],bottom=[50,40,45,35],label='Staff Attorney')
ax.bar([1,2,3,4], [150,130,140,120],bottom=[250,230,225,205],label='Paralegals')


ax.set_xticks([1,2,3,4])
ax.set_xticklabels(['New York', 'California', 'Texas', 'Florida'], rotation=30,ha='right', wrap=True)

plt.title('Number of legal professionals in four states in 2021')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()

plt.savefig('bar chart/png/49.png')
plt.clf()
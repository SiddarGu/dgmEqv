
import matplotlib.pyplot as plt

# create figure
fig = plt.figure(figsize=(15, 8))

# get data
x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']
y1 = [2, 3, 4, 5, 6, 6, 7, 8, 9, 9]
y2 = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]

# plotting figure
ax = plt.subplot()
ax.plot(x, y1, marker='o', label='Facebook User(million)')
ax.plot(x, y2, marker='o', label='Twitter User(million)')

# labeling
ax.set_title('Growth of Social Media Users in 2020', fontsize=25)
ax.set_xlabel('Month', fontsize=20)
ax.set_ylabel('Users(million)', fontsize=20)
ax.set_xticks(x)

# annotate
for xy in zip(x, y1):
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
for xy in zip(x, y2):
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

# legend
ax.legend()

# grids
ax.grid(True, color='black', linestyle='-', linewidth=0.5, alpha=0.3)

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('line chart/png/3.png')

# clear figure
plt.clf()
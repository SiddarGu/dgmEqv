
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
labels = ['USA', 'UK', 'Germany', 'France']
manu = [700, 650, 750, 800]
agri = [500, 550, 650, 750]
serv = [400, 450, 500, 550]

# set the positions of x-axis
x_pos = [i for i, _ in enumerate(labels)]

# plot the bar
ax.bar(x_pos, manu, width=0.2, label='Manufacturing', color='green')
ax.bar([p + 0.2 for p in x_pos], agri, width=0.2, label='Agriculture', color='blue')
ax.bar([p + 0.4 for p in x_pos], serv, width=0.2, label='Services', color='red')

# label the x-axis
ax.set_xlabel('Countries')
ax.set_xticks([p + 0.2 for p in x_pos])
ax.set_xticklabels(labels)

# add a legend
ax.legend(loc='upper center')

# add a title
ax.set_title('Manufacturing, Agriculture and Services output in four countries in 2021')

# Annotate the value of each data point
for i, v in enumerate(manu):
    ax.text(x_pos[i] - 0.1, v + 10, str(v), color='green', fontweight='bold')
for i, v in enumerate(agri):
    ax.text(x_pos[i] + 0.1, v + 10, str(v), color='blue', fontweight='bold')
for i, v in enumerate(serv):
    ax.text(x_pos[i] + 0.3, v + 10, str(v), color='red', fontweight='bold')

# adjust the size of the figure
plt.tight_layout()

# save the figure
plt.savefig('Bar Chart/png/600.png', dpi=600)

# clear the current image state
plt.clf()
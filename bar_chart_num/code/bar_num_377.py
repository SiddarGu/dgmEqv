
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)
ax.bar(['USA', 'UK', 'Germany', 'France'], [500, 450, 400, 350], label='Online Orders', bottom=0)
ax.bar(['USA', 'UK', 'Germany', 'France'], [1000, 950, 900, 850], label='In-Store Orders', bottom=500)
for xpos, ypos, yval in zip(range(4), [500, 450, 400, 350], [500, 450, 400, 350]):
    ax.annotate(yval, xy=(xpos, ypos+yval/2), ha='center', va='center')
for xpos, ypos, yval in zip(range(4), [1000, 950, 900, 850], [1000, 950, 900, 850]):
    ax.annotate(yval, xy=(xpos, ypos+yval/2), ha='center', va='center')
ax.set_title('Comparison of online and in-store orders in four countries in 2021')
ax.set_xticks(range(4))
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'])
ax.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/67.png')
plt.clf()
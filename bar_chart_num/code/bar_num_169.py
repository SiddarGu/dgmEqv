
fig, ax = plt.subplots()
x = np.arange(4)
bar_width = 0.2
ax.bar(x, [7.2, 7.4, 7.6, 7.8], width=bar_width, label='Gender Equality')
ax.bar(x + bar_width, [7.8, 8.0, 8.2, 8.4],width=bar_width, label='Education')
ax.bar(x + 2*bar_width, [7.5, 7.7, 7.9, 8.1], width=bar_width, label='Healthcare')
ax.set_xticks(x + bar_width)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'])
ax.set_title('Level of government and public policies in four countries in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),  shadow=True, ncol=3)
plt.tight_layout()
plt.savefig('Bar Chart/png/516.png')
plt.clf()
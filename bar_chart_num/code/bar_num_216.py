
fig, ax = plt.subplots(figsize=(10,8))

barWidth = 0.3
bars1 = [200, 180, 220, 160]
bars2 = [240, 260, 280, 300]
bars3 = [160, 220, 240, 280]

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

ax.bar(r1, bars1, width=barWidth, label='Manufacturing A(thousand)', color='#0066FF', edgecolor='white')
ax.bar(r2, bars2, width=barWidth, label='Manufacturing B(thousand)', color='#99CC33', edgecolor='white')
ax.bar(r3, bars3, width=barWidth, label='Manufacturing C(thousand)', color='#FF9933', edgecolor='white')

for i, v in enumerate(bars1):
    ax.text(i-0.1, v+0.2, str(v), color='#0066FF', fontweight='bold')
for i, v in enumerate(bars2):
    ax.text(i+0.2, v+0.2, str(v), color='#99CC33', fontweight='bold')
for i, v in enumerate(bars3):
    ax.text(i+0.6, v+0.2, str(v), color='#FF9933', fontweight='bold')

plt.xticks([r + barWidth for r in range(len(bars1))], ['January', 'February', 'March', 'April'])
ax.set_ylabel('Manufacturing(thousand)')
ax.set_title('Manufacturing output in three categories from January to April 2021')
ax.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.savefig("Bar Chart/png/80.png")
plt.clf()
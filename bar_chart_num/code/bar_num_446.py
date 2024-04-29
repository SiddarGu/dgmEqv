
fig, ax = plt.subplots(figsize=(10,6))
x = np.arange(4)

ax.bar(x + 0.00, [1700, 1600, 1400, 1500], color='#FFC300', width=0.25, label='Manufacturing Output(million)')
ax.bar(x + 0.25, [2400, 2200, 2000, 2100], color='#581845', width=0.25, label='Retail Sales(million)')

ax.set_title('Manufacturing output and retail sales in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France']) 
ax.legend()

ax.annotate('1700', xy=(0, 1700), xytext=(0,200), ha='center', va='bottom')
ax.annotate('1600', xy=(1, 1600), xytext=(1,200), ha='center', va='bottom')
ax.annotate('1400', xy=(2, 1400), xytext=(2,200), ha='center', va='bottom')
ax.annotate('1500', xy=(3, 1500), xytext=(3,200), ha='center', va='bottom')

ax.annotate('2400', xy=(0, 2400), xytext=(0,3000), ha='center', va='bottom', rotation=90)
ax.annotate('2200', xy=(1, 2200), xytext=(1,3000), ha='center', va='bottom', rotation=90)
ax.annotate('2000', xy=(2, 2000), xytext=(2,3000), ha='center', va='bottom', rotation=90)
ax.annotate('2100', xy=(3, 2100), xytext=(3,3000), ha='center', va='bottom', rotation=90)

plt.tight_layout()
fig.savefig('Bar Chart/png/595.png')
plt.clf()
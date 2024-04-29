
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.bar(['USA', 'UK', 'Germany', 'France'], [20, 25, 22, 23], width=0.6, bottom=0.0, label='Freight Train', align='center')
ax.bar(['USA', 'UK', 'Germany', 'France'], [30, 35, 32, 33], width=0.6, bottom=20, label='Truck',align='center')
ax.bar(['USA', 'UK', 'Germany', 'France'], [50, 60, 55, 57], width=0.6, bottom=50, label='Air Cargo',align='center')
ax.set_title("Number of freight train, truck and air cargo shipments in four countries in 2021")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
for a, b in zip(['USA', 'UK', 'Germany', 'France'], [20, 25, 22, 23]):
    ax.annotate(str(b), xy=(a, b+2))
for a, b in zip(['USA', 'UK', 'Germany', 'France'], [50, 55, 52, 53]):
    ax.annotate(str(b), xy=(a, b+2))
for a, b in zip(['USA', 'UK', 'Germany', 'France'], [80, 85, 82, 83]):
    ax.annotate(str(b), xy=(a, b+2))  
ax.set_xticks(['USA', 'UK', 'Germany', 'France'])
plt.tight_layout()
plt.savefig('Bar Chart/png/356.png', dpi=300)
plt.clf()
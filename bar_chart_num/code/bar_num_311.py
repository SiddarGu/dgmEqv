
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

Country = ['USA', 'UK', 'Germany', 'France'] 
Tourists = [25000, 30000, 20000, 28000]
Revenue = [1000, 1500, 1200, 1400]

bar1 = ax.bar(Country, Tourists, color='#0099ff', label='Tourists')
bar2 = ax.bar(Country, Revenue, bottom=Tourists, color='#ff6600', label='Revenue(million)')

ax.set_title('Number of tourists and revenue in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend()

for i in range(len(Country)):
    ax.annotate(str(Tourists[i]), xy=(bar1[i].get_x() + bar1[i].get_width() /2, bar1[i].get_height()), xytext=(0, 5), textcoords="offset points", ha='center', va='bottom')
    ax.annotate(str(Revenue[i]), xy=(bar2[i].get_x() + bar2[i].get_width() /2, bar2[i].get_height() + bar1[i].get_height()), xytext=(0, 5), textcoords="offset points", ha='center', va='bottom')

plt.xticks(Country)
plt.tight_layout()
plt.savefig('Bar Chart/png/281.png')
plt.clf()
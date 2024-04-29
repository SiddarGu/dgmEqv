
fig = plt.figure()
ax = fig.add_subplot()
ax.bar(['January', 'February', 'March', 'April'], [500, 650, 750, 550], label='Solar Energy(MW)', width=0.3, bottom=0)
ax.bar(['January', 'February', 'March', 'April'], [600, 700, 800, 900], label='Wind Energy(MW)', width=0.3, bottom=500)
ax.bar(['January', 'February', 'March', 'April'], [400, 500, 600, 700], label='Hydropower(MW)', width=0.3, bottom=1300)
ax.set_title("Renewable energy production in four months of 2021")
ax.legend(loc='upper center')
ax.set_xticks(['January', 'February', 'March', 'April'])
ax.set_xlabel("Month")
ax.set_ylabel("Energy Production(MW)")
ax.set_ylim(0,1900)
for x,y in zip(['January', 'February', 'March', 'April'],[500, 650, 750, 550]):
    ax.annotate(y, xy=(x,y), xytext=(0,10), textcoords='offset points', ha='center', va='bottom')
for x,y in zip(['January', 'February', 'March', 'April'],[600, 700, 800, 900]):
    ax.annotate(y, xy=(x,y), xytext=(0,10), textcoords='offset points', ha='center', va='bottom')
for x,y in zip(['January', 'February', 'March', 'April'],[400, 500, 600, 700]):
    ax.annotate(y, xy=(x,y), xytext=(0,10), textcoords='offset points', ha='center', va='bottom')
plt.tight_layout()
fig.savefig('Bar Chart/png/500.png')
plt.clf()
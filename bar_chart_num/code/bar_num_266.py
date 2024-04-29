
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
ax.bar('USA', [400,350,500], label='Literature', bottom=0, color='red')
ax.bar('USA', [350,420,450], label='Philosophy', bottom=400, color='green')
ax.bar('USA', [500,400,400], label='History', bottom=750, color='blue')
ax.bar('UK', [380,420,450], label='Literature', bottom=0, color='red')
ax.bar('UK', [420,400,400], label='Philosophy', bottom=380, color='green')
ax.bar('UK', [450,380,430], label='History', bottom=800, color='blue')
ax.bar('Germany', [360,400,400], label='Literature', bottom=0, color='red')
ax.bar('Germany', [400,380,430], label='Philosophy', bottom=360, color='green')
ax.bar('Germany', [400,400,430], label='History', bottom=760, color='blue')
ax.bar('France', [340,380,430], label='Literature', bottom=0, color='red')
ax.bar('France', [380,400,430], label='Philosophy', bottom=340, color='green')
ax.bar('France', [430,430,430], label='History', bottom=720, color='blue')

ax.set_xticks(['USA','UK','Germany','France'])
ax.set_xlabel('Country')
ax.set_ylabel('Number of Books Published')
ax.set_title('Number of books published in Social Sciences and Humanities in four countries in 2021')
ax.legend(loc='upper left')

for x,y in zip(['USA','UK','Germany','France'], [400,350,500,380,420,450,360,400,400,340,380,430]):
    ax.annotate(str(y), xy=(x,y), xytext=(0,5), textcoords='offset points', ha='center')
for x,y in zip(['USA','UK','Germany','France'], [750,800,760,720]):
    ax.annotate(str(y), xy=(x,y), xytext=(0,5), textcoords='offset points', ha='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/515.png')
plt.clf()
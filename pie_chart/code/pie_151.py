
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

data = {'Platforms':['Facebook','Instagram','Twitter','YouTube','LinkedIn','Snapchat','Other'],
        'Usage Rate':[30,20,15,15,10,5,5]}

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.set_title('Popular Social Media Platforms Usage in 2023')

wedges, texts, autotexts = ax.pie(data['Usage Rate'], 
                                  labels=data['Platforms'],
                                  autopct='%.2f%%',
                                  textprops={'fontsize':14},
                                  wedgeprops={'linewidth':2},
                                  startangle=90)

ax.legend(wedges, data['Platforms'],
          title='Platforms',
          loc='center left',
          bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=14)
ax.axis('equal')
ax.set_xticks([])
ax.set_yticks([])
plt.tight_layout()
plt.savefig('pie chart/png/33.png')
plt.clf()

import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
ax=plt.subplot()
ax.set_title('Number of sports teams and viewers in four countries in 2021')
country=['USA','UK','Germany','France']
teams=[20,25,30,15]
viewers=[15000,14000,13000,12000]
ax.bar(country,teams,label='Sports Teams')
ax.bar(country,viewers,bottom=teams,label='Viewers')
ax.set_xticklabels(country,rotation=45, wrap=True)
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/212.png')
plt.clf()
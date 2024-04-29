
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
labels = ['Single Family Homes','Townhomes','Condominiums','Mobile Homes','Multi-Family Housing']
sizes = [45,20,15,10,10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 2, 'edgecolor': 'white'})
plt.title('Distribution of Housing Types in the USA, 2023')
plt.axis('equal') 
plt.legend(labels, loc="best", bbox_to_anchor=(1,0,0.5,1))
plt.savefig('pie chart/png/315.png', bbox_inches='tight')
plt.tight_layout()
plt.xticks([])
plt.clf()
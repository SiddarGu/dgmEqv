
import matplotlib.pyplot as plt
import matplotlib

fig = plt.figure(figsize=(8,8)) 
ax = fig.add_subplot(111) 

causes = ['Education', 'Health', 'Poverty', 'Environment', 'Human Rights'] 
percent = [25, 20, 30, 15, 10] 

ax.pie(percent, labels=causes, startangle=90, autopct='%1.1f%%', shadow=True, radius=1.2, textprops={'fontsize': 10, 'wrap': True})
plt.title("Distribution of Donations to Charitable Causes in the US, 2023", fontsize=14)
plt.tight_layout() 
plt.xticks(rotation=45) 

plt.savefig('pie chart/png/316.png', bbox_inches='tight')
plt.clf()

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

Platforms = ['Facebook','Twitter','YouTube','Instagram','LinkedIn','Pinterest','Snapchat']
Percentage = [32,15,25,14,7,4,3]

ax.pie(Percentage,labels=Platforms, autopct='%1.1f%%', textprops={'fontsize': 15}, 
       shadow=True, startangle=90, explode=(0, 0.1, 0, 0, 0, 0, 0))

ax.set_title("Major Social Media Platforms Utilization in the US, 2023", fontsize=20)

ax.legend(Platforms, loc='upper left', bbox_to_anchor=(-0.1, 1.), fontsize=15) 
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/307.png')
plt.close()
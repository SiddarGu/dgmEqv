
import matplotlib.pyplot as plt

fields = ['Physical Sciences','Life Sciences','Engineering','Computer Science','Mathematics','Other']
percentage = [25,25,20,15,10,5]

plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.pie(percentage, labels=fields,autopct='%1.1f%%',textprops={'fontsize': 12})
ax.axis('equal') 
ax.set_title('Distribution of Research Fields in Science and Engineering, 2023')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/76.png')
plt.clf()
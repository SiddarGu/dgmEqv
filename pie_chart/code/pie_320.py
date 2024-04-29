
import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
ax=plt.subplot()
Areas=['Biological Sciences','Physics','Chemistry','Mathematics','Computer Science','Earth Science','Aerospace Engineering']

Percentage=[25,20,20,15,10,5,5]

ax.pie(Percentage,labels=Areas,autopct='%1.1f%%')
plt.title('Percentage Distribution of Science and Engineering Fields in Higher Education, 2023',fontsize=14)
plt.tight_layout()
plt.xticks(rotation=45)

plt.savefig('pie chart/png/279.png')
plt.clf()
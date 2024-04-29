
import matplotlib.pyplot as plt

labels=['Primary','Secondary','Tertiary','Vocational']
values=[45,25,20,10]

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot()
ax.pie(values,labels=labels,autopct='%1.1f%%',startangle=90,textprops={'fontsize': 14},shadow=True,explode=[0.1,0,0,0])
ax.set_title('Distribution of Education Levels in the USA, 2023', fontsize=16,pad=10)
plt.tight_layout()
plt.savefig('pie chart/png/479.png')
plt.clf()
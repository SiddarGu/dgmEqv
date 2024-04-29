
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
plt.title('Breakdown of Scientific Fields in Academia, 2023')
subplot=plt.subplot()
labels=['Physics','Chemistry','Mathematics','Computer Science','Engineering','Medicine','Astronomy','Ecology']
values=[20,20,10,15,15,10,5,5]
colors=['#FF0000','#00FF00','#0000FF','#FFFF00','#FF00FF','#00FFFF','#800000','#008080']
explode=[0.1,0,0,0,0,0,0,0]
subplot.pie(values, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
subplot.axis('equal')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/347.png')
plt.clf()
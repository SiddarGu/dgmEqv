
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
labels = ['High School Diploma','Associate\'s Degree','Bachelor\'s Degree','Master\'s Degree','Doctoral Degree']
sizes = [35,20,27,14,4]
explode = (0.1,0,0,0,0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 10, 'rotation': 90, 'wrap': True})
        
plt.axis('equal')
plt.title('Educational Attainment of US Adults in 2023')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/496.png')
plt.clf()

import matplotlib.pyplot as plt

plt.figure(figsize=(7,7))

labels = ['Primary Education','Secondary Education','Higher Education','Vocational Training','Non Formal Education']
sizes = [45,30,15,5,5]
explode = (0.1,0,0,0,0)

patches, l_text, p_text = plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True, startangle=90,textprops={'fontsize':10,'rotation':45,'ha':'right','wrap':True})

for t in l_text:
    t.set_size=(30)
for t in p_text:
    t.set_size=(20)

plt.title('Breakdown of Student Population by Level of Education in 2023', fontsize=20)

plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=45)

plt.savefig('pie chart/png/460.png')
plt.clf()
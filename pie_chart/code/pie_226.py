
import matplotlib.pyplot as plt
import matplotlib as mpl

#draw pie chart
plt.figure(figsize=(7,7))
plt.title("Energy Sources Distribution in the USA, 2023")
labels = ['Fossil Fuels','Renewables','Nuclear','Other']
sizes = [40,45,10,5]
explode = (0.1,0,0,0)
colors = ["#FF7F50",'#87CEEB','#AFEEEE','#CDCD00']
mpl.rcParams['font.size'] = 10
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
plt.pie(sizes,labels=labels,autopct='%1.1f%%',explode=explode,shadow=True,colors=colors,startangle=90,pctdistance=0.6,labeldistance=1.1,textprops={'fontsize':10})
plt.legend(labels,loc="best",frameon=False,bbox_to_anchor=(1.3,1))
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pie chart/png/271.png')
plt.clf()
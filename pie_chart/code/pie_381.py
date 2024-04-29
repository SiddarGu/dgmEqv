
import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
sources = ['Solar','Wind','Hydro','Nuclear','Geothermal'] 
percentage = [25,20,30,15,10]
explode = (0.1,0,0,0,0)
plt.pie(percentage,explode=explode,labels=sources,autopct='%1.1f%%',shadow=True,startangle=90,textprops={'fontsize': 8,'rotation':90,'wrap':True})
plt.title('Distribution of Renewable Energy Sources in the USA, 2023',fontsize=14)
plt.tight_layout()
plt.xticks(fontsize=12)
plt.savefig('pie chart/png/196.png')
plt.close()
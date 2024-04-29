
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
ax=plt.subplot()

causes=["Education","Animal Welfare","Disaster Relief","Poverty Alleviation","Health and Wellness","Environmental Conservation","Other"]
percentages=[25,15,15,15,15,15,5]

colors=["#36B7B7","#FF4B4B","#FFC300","#FFEF4B","#5AFF4B","#6BFFB7","#A4FFCF"]
ax.pie(percentages,labels=causes,autopct="%1.1f%%",colors=colors,startangle=90,textprops={'fontsize':14, 'wrap':True,'rotation':45})
plt.title("Distribution of Charitable Donations Worldwide in 2023",fontsize=18)
plt.tight_layout()
plt.savefig("pie chart/png/60.png")
plt.clf()
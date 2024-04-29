
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
labels=["Pop","Rock","Jazz","Classical","Country","Hip-Hop","Electronic","Reggae","Other"]
sizes=[20,15,10,25,10,10,5,5,10]
explode=[0,0.1,0,0,0,0,0,0,0]
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",shadow=False,labeldistance=1.2)
plt.title("Distribution of Music Genres in the United States, 2023",fontsize=15,fontweight="bold")
plt.tight_layout()
plt.savefig("pie chart/png/184.png")
plt.clf()
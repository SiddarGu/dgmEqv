
import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
labels = ["Food Banks","Medical Research","Homeless Shelters","Animal Rescue","Education Programs","Humanitarian Aid"]
sizes = [20,15,20,15,15,15]
explode = (0.1,0,0,0,0,0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%', startangle=90)
plt.title("Distribution of Donations to Charities in the US, 2023")
plt.axis('equal')
plt.xticks(rotation = 90, wrap=True)
plt.tight_layout()
plt.savefig("pie chart/png/53.png")
plt.clf()
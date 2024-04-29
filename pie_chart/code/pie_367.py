
import matplotlib.pyplot as plt

labels = ["Corporate Law","Tax Law","Employment Law","Criminal Law","International Law","Intellectual Property Law","Environmental Law","Other"]
sizes = [25,20,20,15,10,10,5,5]

plt.figure(figsize=(10,10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
plt.title("Distribution of Law Practices in the USA, 2023", fontsize=14, fontweight='bold')
plt.legend(labels, loc="best", bbox_to_anchor=(1,0,0.5,1),fontsize='large')
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/90.png')
plt.clf()
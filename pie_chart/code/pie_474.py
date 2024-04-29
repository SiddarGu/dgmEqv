
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()
percentages = [20, 15, 30, 15, 10, 10]
laws = ["Constitutional Law", "Contract Law", "Criminal Law", "Tax Law", "Human Rights Law", "Tort Law"]
plt.pie(percentages, labels=laws, autopct='%1.1f%%', startangle=90, textprops={'wrap': True, 'rotation': 0, 'fontsize': 16})
plt.title('Distribution of Laws in the United States, 2023', fontsize=20)
plt.tight_layout()
plt.savefig('pie chart/png/244.png')
plt.clf()
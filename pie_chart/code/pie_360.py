
import matplotlib.pyplot as plt
label = ["Personal Injury", "Civil Litigation", "Product Liability", "Intellectual Property", "Employment", "Criminal"]
sizes = [20, 25, 15, 20, 10, 10]
explode = [0, 0, 0, 0, 0, 0]
plt.figure(figsize=(6,6))
plt.pie(sizes, explode=explode, labels=label, autopct="%.1f%%", shadow=True, startangle=90)
plt.title("Types of Lawsuits in the US in 2023", fontsize=14, fontweight="bold")
plt.legend(bbox_to_anchor=(1, 0.5), loc="center right", fontsize=10)
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig("pie chart/png/300.png")
plt.clf()
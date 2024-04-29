
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
values = [50, 30, 10, 5, 5]
labels = ["Full-time", "Part-time", "Contractors", "Interns", "Freelancers"]
plt.pie(values, labels=labels, autopct="%1.1f%%", shadow=True, rotatelabels=True, startangle=90)
plt.title("Proportion of Employee Types in the USA, 2023")
plt.tight_layout()
plt.savefig("pie chart/png/216.png")
plt.clf()

import matplotlib.pyplot as plt

labels = ["Animal Welfare", "Education", "Humanitarianism", "Healthcare", "Arts & Culture"]
sizes = [20, 25, 30, 15, 10]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", wedgeprops={"edgecolor": "black"}, textprops={'fontsize': 14, 'wrap': True, 'rotation': 45})

ax.set_title("Allocation of Donations for Non-profit Organizations in the US, 2023")

plt.tight_layout()
plt.savefig('pie chart/png/215.png')
plt.clf()